from datetime import date

from pydantic import BaseModel


class Booking(BaseModel):
    id: int
    room_id: int
    account_id: int
    date_from: date
    date_to: date
    price: int
    total_days: int
    total_cost: int
