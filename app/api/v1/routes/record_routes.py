from fastapi import APIRouter, Depends

from app.core import config
from app.database.database import get_async_db, AsyncSession
from app.database.repository.record_repository import RecordRepository

record_router = APIRouter(
    prefix="/records",
    tags=["Records"],
)


@record_router.get("/")
async def get_keys(
    db: AsyncSession = Depends(get_async_db)
):
    repository = RecordRepository(db)
    # print(config.database_url())
    return await repository.get_all()


@record_router.post("/")
async def create_key():
    return {"message": "Create key"}


@record_router.put("/{id}")
async def update_key(id: int):
    return {"message": f"Update key {id}"}


@record_router.delete("/{id}")
async def delete_key(id: int):
    return {"message": f"Delete key {id}"}
