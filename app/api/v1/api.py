
from fastapi import APIRouter
from app.api.v1.routes.key_routes import key_router
from app.api.v1.routes.record_routes import record_router
from app.api.v1.routes.seed import seed_router

routers = [
    key_router,
    record_router,
    seed_router,
]

v1_router = APIRouter()

for router in routers:
    v1_router.include_router(router)
