from fastapi import FastAPI

from src.booking.router import router as booking_router


app = FastAPI()

app.include_router(booking_router)
