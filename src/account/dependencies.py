from datetime import datetime

from fastapi import Request, HTTPException, status, Depends
from jose import jwt, JWTError

from config import settings
from src.account.models import Account
from src.account.service import AccountService


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
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is not valid')

    expire: str = payload.get('exp')
    if not expire or (int(expire) < datetime.utcnow().timestamp()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is expired')

    account_id: str = payload.get('sub')
    if not account_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token has not "sub" parameter')

    account = await AccountService.find_by_id(int(account_id))
    if not account:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Account does not exists')

    return account
