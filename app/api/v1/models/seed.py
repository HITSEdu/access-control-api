from pydantic import BaseModel


class SeedAndId(BaseModel):
    id: int
    seed: str
