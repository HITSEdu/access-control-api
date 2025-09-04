from fastapi import APIRouter, Depends
from app.services.seed import generate_crypto_seed

seed_router = APIRouter(prefix="/seed", tags=["Seed"])


@seed_router.get("/get_seed")
async def get_seed():
    seed = generate_crypto_seed()
        
