from sqlalchemy import Column, Integer, String
from src.database.core import Base


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
