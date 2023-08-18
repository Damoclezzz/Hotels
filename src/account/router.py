from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Response, Depends

from src.account.dependencies import get_current_account
from src.account.schemas import AccountBase, CreateAccount, AuthAccount, Token
from src.account.service import AccountService as Service
from src.account.models import Account


router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)


@router.post('/register', response_model=AccountBase)
async def create_account(account_data: CreateAccount):
    if await Service.find_one_or_none(email=account_data.email) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Account with this email already exists')

    return await Service.create_account(account_data)


@router.post('/login', response_model=Token)
async def login(account_data: AuthAccount, response: Response):
    account = await Service.authenticate(account_data)

    return Token(token=Service.set_token(account, response))


@router.post('/logout')
async def logout(response: Response):
    Service.delete_token(response)


@router.get('/account', response_model=AccountBase)
async def get_account(current_account: Annotated[Account, Depends(get_current_account)]):
    return current_account
