from sqlalchemy import UUID, Column
from app.database.database import Base
from sqlalchemy.orm import relationship
import uuid
from app.database.models import key_lock_association


class Lock(Base):
    __tablename__ = "lock"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    keys = relationship("key", secondary=key_lock_association, backref="locks")
