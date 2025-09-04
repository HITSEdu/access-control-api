from sqlalchemy import Column, String, BigInteger
from app.database.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Key(Base):
    __tablename__ = "key"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    seed = Column(String, nullable=False)
    time = Column(BigInteger, nullable=False)
