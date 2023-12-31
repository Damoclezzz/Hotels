from typing import Optional

from fastapi import Response

from src.exceptions.auth.credentials import IncorrectLoginOrPasswordException, AccountNotExistsException

from src.database.service import BaseRepository
from src.account.models import Account
from src.account.schemas import CreateAccount, AuthAccount
from src.account.auth import get_password_hash, verify_password, create_access_token


class AccountService:
    repository = BaseRepository(Account)

    @classmethod
    async def create_account(cls, account_data: CreateAccount):
        hashed_password = get_password_hash(account_data.password)

        account = Account(
            email=account_data.email,
            hashed_password=hashed_password,
        )

        return await cls.repository.add(account)

    @classmethod
    async def authenticate(cls, account_data: AuthAccount) -> Account:
        account: Optional[Account] = await cls.repository.find_one_or_none(email=account_data.email)
        if not account:
            raise AccountNotExistsException()

        is_valid_password = verify_password(account_data.password, account.hashed_password)
        if not is_valid_password:
            raise IncorrectLoginOrPasswordException()

        return account

    @classmethod
    def set_token(cls, account: Account, response: Response) -> str:
        access_token = create_access_token({'sub': str(account.id)})
        response.set_cookie("booking_access_token", access_token, httponly=True)

        return access_token

    @classmethod
    def delete_token(cls, response: Response) -> None:
        response.delete_cookie('booking_access_token')
