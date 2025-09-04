from fastapi import APIRouter

key_router = APIRouter(
    prefix="/keys",
    tags=["Keys"],
)


@key_router.get("/")
async def get_keys():
    return {"message": "Get all keys"}


@key_router.post("/")
async def create_key():
    return {"message": "Create key"}


@key_router.put("/{id}")
async def update_key(id: int):
    return {"message": f"Update key {id}"}


@key_router.delete("/{id}")
async def delete_key(id: int):
    return {"message": f"Delete key {id}"}
