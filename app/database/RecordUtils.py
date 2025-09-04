from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RecordBase(BaseModel):
    user_id: int
    status: str
    door_id: Optional[str] = None
    access_type: Optional[str] = None
    reason: Optional[str] = None

class RecordCreate(RecordBase):
    pass

class RecordUpdate(BaseModel):
    status: Optional[str] = None
    reason: Optional[str] = None

class RecordResponse(RecordBase):
    id: int
    access_time: datetime
    
    class Config:
        from_attributes = True