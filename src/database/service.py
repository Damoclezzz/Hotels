from sqlalchemy import select

from src.database.core import async_session_maker, Base
from typing import Type


class BaseRepository:
    model: Type[Base] = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            return await session.get(cls.model, model_id)

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.c).filter_by(**filter_by)

            result = await session.execute(query)

            return result.one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.c).filter_by(**filter_by)

            result = await session.execute(query)

            return result.all()

    @classmethod
    async def add(cls, data: Base):
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()

            await session.refresh(data)

            return data
