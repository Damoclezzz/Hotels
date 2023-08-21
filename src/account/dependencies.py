from datetime import datetime

from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from config import settings
from src.account.models import Account
from src.account.service import AccountService
from src.exceptions import (
    TokenNotValidException, TokenExpiredException, TokenSubKeyNotExists, AccountNotExistsException
)


def get_token(request: Request):
    token = request.cookies.get('booking_access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User does not authorized')
    return token


async def get_current_account(access_token: str = Depends(get_token)) -> Account:
    try:
        payload = jwt.decode(
            access_token, settings.TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM
        )
    except JWTError:
        raise TokenNotValidException()

    expire: str = payload.get('exp')
    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenExpiredException()

    account_id: str = payload.get('sub')
    if not account_id:
        raise TokenSubKeyNotExists()

    account = await AccountService.find_by_id(int(account_id))
    if not account:
        raise AccountNotExistsException()

    return account
