from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database.database import Base

class Key(Base):
    __tablename__ = "key"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    