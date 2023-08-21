from sqlalchemy import select

from src.database.core import async_session_maker, Base
from typing import Type


class BaseRepository:
    def __init__(self, model: Type[Base]):
        self.model = model

    async def find_by_id(self, model_id: int):
        async with async_session_maker() as session:
            return await session.get(self.model, model_id)

    async def find_one_or_none(self, **filter_by):
        async with async_session_maker() as session:
            query = select(self.model.__table__.c).filter_by(**filter_by)

            result = await session.execute(query)

            return result.one_or_none()

    async def find_all(self, **filter_by):
        async with async_session_maker() as session:
            query = select(self.model.__table__.c).filter_by(**filter_by)

            result = await session.execute(query)

            return result.all()

    @staticmethod
    async def add(data: Base):
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()

            await session.refresh(data)

            return data
