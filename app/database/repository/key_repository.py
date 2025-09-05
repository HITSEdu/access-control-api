from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select, update, delete
from app.database.models.key import Key


class KeyRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> Key:
        key = Key(
            seed=data["seed"],
            time=data["time"],
        )
        self.session.add(key)
        await self.session.commit()
        await self.session.refresh(key)
        return key
    
    async def has_key(self, lock_id: UUID, key_id: UUID) -> bool:
        result = await self.session.execute(
            select(exists()
                .select_from(key_lock_association)
                .where(
                    key_lock_association.c.lock_id == lock_id,
                    key_lock_association.c.key_id == key_id
                )
            )
        )
        return result.scalar()

    async def delete(self, id: int) -> bool:
        ...

    async def update(self, id: int, data: dict) -> Optional[Record]:
        ...

    async def get_all(self) -> List[...]:
        ...

    async def get_by_id(self, id: int) -> List[...]:
        ...
