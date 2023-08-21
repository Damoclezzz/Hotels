from fastapi import APIRouter, Depends

from src.account.models import Account
from src.booking.service import BookingService as Service
from src.booking.schemas import Booking
from src.account.dependencies import get_current_account


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings']
)


@router.get('')
async def get_bookings(account: Account = Depends(get_current_account)) -> list[Booking]:
    return await Service.repository.find_all(account_id=account.id)


@router.get('/{booking_id}')
async def get_booking(booking_id: int):
    return await Service.repository.find_by_id(booking_id)
