from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from src.database import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSONB)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
