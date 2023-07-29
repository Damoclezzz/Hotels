from fastapi import APIRouter

from sqlalchemy import select

from src.database import async_session_maker
from src.booking.models import Booking


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Booking.__table__.columns)

        result = await session.execute(query)

        return result.mappings().all()
