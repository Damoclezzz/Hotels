from fastapi import APIRouter

from src.booking.service import BookingService
from src.booking.schemas import SBooking


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings() -> list[SBooking]:
    return await BookingService.find_all()


@router.get('/{booking_id}')
async def get_booking(booking_id: int):
    return await BookingService.find_by_id(booking_id)
