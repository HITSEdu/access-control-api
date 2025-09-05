from uuid import UUID
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

# Ваши Pydantic модели
class Lock(BaseModel):
    id: UUID
    keys: List[UUID]

class Key(BaseModel):
    id: UUID
    seed: str
    time: int

# Модели для создания (без ID, так как он генерируется автоматически)
class KeyCreate(BaseModel):
    seed: str
    time: int

class LockCreate(BaseModel):
    keys: List[UUID] = []  # опционально, можно создать замок без ключей

# Роутер
admin_router = APIRouter(prefix="/admin", tags=["admin"])

# Зависимость для получения сессии БД (предполагается, что у вас есть get_async_db)
# from app.database.database import get_async_db

@admin_router.post("/keys", response_model=Key, status_code=status.HTTP_201_CREATED)
async def create_key(
    key_data: KeyCreate,
    db: AsyncSession = Depends(get_async_db),
) -> Key:
    """
    Создает новый ключ
    """
    try:
        key_repo = KeyRepository(db)
        
        # Создаем ключ в базе
        created_key = await key_repo.create({
            "seed": key_data.seed,
            "time": key_data.time
        })
        
        # Возвращаем ключ в формате Pydantic модели
        return Key(
            id=created_key.id,
            seed=created_key.seed,
            time=created_key.time
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при создании ключа: {str(e)}"
        )

@admin_router.post("/locks", response_model=Lock, status_code=status.HTTP_201_CREATED)
async def create_lock(
    lock_data: LockCreate,
    db: AsyncSession = Depends(get_async_db),
) -> Lock:
    """
    Создает новый замок с опциональным списком ключей
    """
    try:
        lock_repo = LockRepository(db)
        key_repo = KeyRepository(db)
        
        # Проверяем, что все указанные ключи существуют
        if lock_data.keys:
            existing_keys = await key_repo.get_by_ids(lock_data.keys)
            existing_key_ids = {key.id for key in existing_keys}
            
            # Проверяем, есть ли несуществующие ключи
            non_existing_keys = set(lock_data.keys) - existing_key_ids
            if non_existing_keys:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Ключи не найдены: {non_existing_keys}"
                )
        
        # Создаем замок (предполагается, что метод create в LockRepository 
        # принимает данные и обрабатывает связи с ключами)
        created_lock = await lock_repo.create({
            "keys": lock_data.keys
        })
        
        # Если метод create не обрабатывает связи, нужно добавить отдельную логику
        # для установки связей между замком и ключами
        
        # Получаем полные данные замка с ключами
        full_lock = await lock_repo.get_by_id(created_lock.id)
        if not full_lock:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Замок не найден после создания"
            )
        
        # Возвращаем замок в формате Pydantic модели
        return Lock(
            id=full_lock.id,
            keys=[key.id for key in full_lock.keys]  # список UUID ключей
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ошибка при создании замка: {str(e)}"
        )

# Дополнительно: можно добавить метод для получения всех ключей/замков
@admin_router.get("/keys", response_model=List[Key])
async def get_all_keys(
    db: AsyncSession = Depends(get_async_db),
) -> List[Key]:
    """
    Получает все ключи
    """
    key_repo = KeyRepository(db)
    keys = await key_repo.get_all()
    
    return [
        Key(id=key.id, seed=key.seed, time=key.time)
        for key in keys
    ]

@admin_router.get("/locks", response_model=List[Lock])
async def get_all_locks(
    db: AsyncSession = Depends(get_async_db),
) -> List[Lock]:
    """
    Получает все замки
    """
    lock_repo = LockRepository(db)
    locks = await lock_repo.get_all()
    
    return [
        Lock(id=lock.id, keys=[key.id for key in lock.keys])
        for lock in locks
    ]