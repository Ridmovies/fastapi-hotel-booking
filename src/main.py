from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.dev.router import dev_router
from src.users.router import user_router
from src.hotels.router import hotel_router
from src.bookings.router import booking_router
from src.rooms.router import room_router
from src.auth.router import auth_router
from src.pages.router import page_router
from src.images.router import image_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(hotel_router, prefix="/hotel", tags=["hotel"])
app.include_router(booking_router, prefix="/booking", tags=["booking"])
app.include_router(room_router, prefix="/room", tags=["room"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(page_router, prefix="/page", tags=["page"])
app.include_router(image_router, prefix="/image", tags=["image"])

app.include_router(dev_router, prefix="/dev", tags=["dev"])



@app.get("/")
async def root():
    return {"message": "Hello World"}