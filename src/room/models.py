from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from src.database.core import Base


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotel.id'))
    name = Column(String, nullable=False)
    description = Column(Text)
    services = Column(JSONB)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    image_id = Column(Integer)
