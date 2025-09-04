from pydantic import BaseModel
from uuid import UUID


class Record(BaseModel):
    id: int
    status: str
    lock_id: UUID
    key_id: UUID
