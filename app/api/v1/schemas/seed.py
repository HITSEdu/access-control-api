from uuid import UUID
from pydantic import BaseModel


class SeedAndId(BaseModel):
    id: UUID
    seed: str
