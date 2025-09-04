from typing import List, Optional
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select, update, delete
from app.database.models.lock import Lock
from app.database.models.record import Record


class LockRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, data: dict) -> Lock:
        ...

    async def delete(self, id: int) -> bool:
        ...

    async def update(self, id: int, data: dict) -> Optional[Record]:
        ...

    async def get_all(self) -> List[Lock]:
        ...

    async def get_by_id(self, id: UUID) -> Optional[Lock]:
        result = await self.session.execute(
            select(Lock)
            .where(Lock.id == id)
        )
        return result.scalar_one_or_none()
