from sqlalchemy import UUID, Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base
import uuid


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    access_time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status = Column(String, nullable=False)  # 'success', 'failed', 'denied'
    lock_id = Column(UUID(as_uuid=True), nullable=False, index=True)
