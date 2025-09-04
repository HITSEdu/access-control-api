from sqlalchemy import Table, Column, ForeignKey
from app.database.database import Base

key_lock_association = Table(
    'key_lock_association',
    Base.metadata,
    Column('key_id', ForeignKey('key.id'), primary_key=True),
    Column('lock_id', ForeignKey('lock.id'), primary_key=True)
)
