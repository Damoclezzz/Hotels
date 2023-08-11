from pydantic import BaseModel, EmailStr, field_validator, Field

from src.utils.validators.string import StringValidator


class AccountBase(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str


class CreateAccount(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=25)

    @classmethod
    @field_validator('password')
    def validate_password(cls, password: str):
        if not StringValidator.contains_digit(password):
            raise ValueError('Password must contains digest')
        if not StringValidator.contains_upper(password):
            raise ValueError('Password must contains 1 upper letter or more')

        return password


class AuthAccount(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    token: str
