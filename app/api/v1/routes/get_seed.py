from fastapi import APIRouter, Depends
from app.api.v1.schemas.seed import SeedAndId
from app.database.database import get_async_db, AsyncSession
from app.database.repository.lock_repository import LockRepository
from app.database.repository.key_repository import KeyRepository
from app.services.seed import generate_crypto_seed
import time

seed_router = APIRouter(prefix="/seed", tags=["Seed"])


@seed_router.get("/get_seed")
async def get_seed(
    db: AsyncSession = Depends(get_async_db)
) -> SeedAndId:
    seed = await generate_crypto_seed()
    current_unix_time = int(time.time())
    repository = KeyRepository(db)
    key = await repository.create(
        {
            "seed": seed,
            "time": current_unix_time,
        }
    )
    return SeedAndId(
        id=key.id,
        seed=seed,
    )


@seed_router.post("/post_seed")
async def send_seed_to_lock(
    key_id: int,
    lock_id: int,
    db: AsyncSession = Depends(get_async_db),
) -> SeedAndId:
    lock_repository = LockRepository(db)
    key_repository = KeyRepository(db)
    key = key_repository.get_by_id(key_id)
    # TODO("post method ")
    
    return ...