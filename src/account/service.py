from typing import Optional

from fastapi import HTTPException, status, Response

from src.database.service import BaseRepository
from src.account.models import Account
from src.account.schemas import CreateAccount, AuthAccount
from src.account.auth import get_password_hash, verify_password, create_access_token


class AccountService(BaseRepository): # TODO: Replace inheritance to var
    model = Account

    @classmethod
    async def create_account(cls, account_data: CreateAccount):
        hashed_password = get_password_hash(account_data.password)

        account = Account(
            email=account_data.email,
            hashed_password=hashed_password,
        )

        return await cls.add(account)

    @classmethod
    async def authenticate(cls, account_data: AuthAccount) -> Account:
        account: Optional[Account] = await cls.find_one_or_none(email=account_data.email)
        if not account:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Account with this email does not exists'
            )

        is_valid_password = verify_password(account_data.password, account.hashed_password)
        if not is_valid_password:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Wrong password')

        return account

    @classmethod
    def set_token(cls, account: Account, response: Response) -> str:
        access_token = create_access_token({'sub': account.id})
        response.set_cookie("booking_access_token", access_token, httponly=True)

        return access_token

