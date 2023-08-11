from fastapi import APIRouter, HTTPException, status, Response

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


@router.get('/{account_id}', response_model=AccountBase)
async def get_account(account_id: int):
    account: Account = await Service.find_one_or_none(id=account_id)

    if account is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Account not found')

    return account
