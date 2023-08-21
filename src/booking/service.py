from src.database.service import BaseRepository
from src.booking.models import Booking


class BookingService:
    repository = BaseRepository(Booking)
