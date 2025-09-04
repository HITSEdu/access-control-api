from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import desc, select, update, delete

from app.database.RecordUtils import RecordCreate, RecordUpdate
from app.database.models.record import Record


class RecordRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, record_data: RecordCreate) -> Record:
        record = Record(**record_data.dict())
        self.session.add(record)
        await self.session.commit()
        await self.session.refresh(record)
        return record

    async def delete(self, record_id: int) -> bool:
        result = await self.session.execute(
            delete(Record).where(Record.id == record_id)
        )
        await self.session.commit()
        return result.rowcount > 0

    async def update(self, record_id: int, record_data: RecordUpdate) -> Optional[Record]:
        record = await self.get_by_id(record_id)
        if not record:
            return None
        update_data = record_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(record, field, value)
        await self.session.commit()
        await self.session.refresh(record)
        return record

    async def get_all(self) -> List[Record]:
        result = await self.session.execute(
            select(Record)
            .order_by(desc(Record.access_time))
        )
        return result.scalars().all()

    async def get_by_status(self, status: str) -> List[Record]:
        result = await self.session.execute(
            select(Record)
            .where(Record.status == status)
            .order_by(desc(Record.access_time))
        )
        return result.scalars().all()

    async def get_by_id(self, id: int) -> List[Record]:
        result = await self.session.execute(
            select(Record)
            .where(Record.id == id)
            .order_by(desc(Record.access_time))
        )
        return result.scalars().all()
