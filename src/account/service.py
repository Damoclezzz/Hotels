from src.database.service import BaseRepository
from src.account.models import Account


class AccountService(BaseRepository):
    model = Account
