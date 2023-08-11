from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

from config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=settings.TOKEN_MINUTES_LIFESPAN)
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(
        to_encode, settings.TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM
    )

    return encoded_jwt
