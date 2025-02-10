from fastapi import FastAPI

from src.dev.router import dev_router
from src.users.router import user_router
from src.hotels.router import hotel_router
from src.bookings.router import booking_router
from src.rooms.router import room_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(hotel_router, prefix="/hotel", tags=["hotel"])
app.include_router(booking_router, prefix="/booking", tags=["booking"])
app.include_router(room_router, prefix="/room", tags=["room"])
app.include_router(dev_router, prefix="/dev", tags=["dev"])



@app.get("/")
async def root():
    return {"message": "Hello World"}