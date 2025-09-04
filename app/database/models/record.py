from sqlalchemy import UUID, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base


class Record(Base):
    __tablename__ = "record"
    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(String, nullable=False)  # 'success', 'failed', 'denied'
    lock_id = Column(UUID(as_uuid=True), ForeignKey('lock.id'), nullable=False)
    key_id = Column(UUID(as_uuid=True), ForeignKey('key.id'), nullable=False)
