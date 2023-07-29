from src.database.service import BaseRepository
from src.booking.models import Booking


class BookingService(BaseRepository):
    model = Booking
