from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Lock(Base):
    __tablename__ = "lock"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    access_time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status = Column(String, nullable=False)  # 'success', 'failed', 'denied'