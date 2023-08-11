from fastapi import FastAPI

from src.booking.router import router as booking_router
from src.account.router import router as account_router


app = FastAPI()

app.include_router(booking_router)
app.include_router(account_router)
