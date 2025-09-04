from typing import List
from pydantic import BaseModel
from uuid import UUID


class Lock(BaseModel):
    id: UUID
    keys: List[UUID]
