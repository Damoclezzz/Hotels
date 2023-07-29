from sqlalchemy import select

from src.database.core import async_session_maker


class BaseRepository:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)

            result = await session.execute(query)

            return result.mappings().all()
