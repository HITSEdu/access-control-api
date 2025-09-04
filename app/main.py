from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text

from app.api.v1.api import v1_router
from app.core.settings import setup_cors
from app.database.database import async_engine, Base, AsyncSession, create_tables, get_async_db

from fastapi import APIRouter, Depends, HTTPException

app = FastAPI()
setup_cors(app)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await async_engine.dispose()


@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_async_db)):
    try:
        result = db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Database error: {str(e)}")


@app.get("/init-db")
async def init_database():
    try:
        await create_tables()
        return {"status": "success", "message": "Database tables created"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Init error: {str(e)}")


app.include_router(v1_router, prefix="/api/v1")
