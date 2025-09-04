from pydantic import BaseModel
from uuid import UUID


class Key(BaseModel):
    id: UUID
    seed: str
    time: int
