from fastapi import APIRouter

from src.booking.service import BookingService


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings():
    return await BookingService.find_all()
