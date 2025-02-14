from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from src.admin.auth import authentication_backend
from src.admin.views import UserAdmin, BookingAdmin, HotelAdmin
from src.database import async_engine
from src.dev.router import dev_router
from src.users.router import user_router
from src.hotels.router import hotel_router
from src.bookings.router import booking_router
from src.rooms.router import room_router
from src.auth.router import auth_router
from src.pages.router import page_router
from src.images.router import image_router

from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)

# admin = Admin(app, async_engine)
admin = Admin(app, async_engine, authentication_backend=authentication_backend)
admin.add_view(UserAdmin)
admin.add_view(BookingAdmin)
admin.add_view(HotelAdmin)


app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(hotel_router, prefix="/hotel", tags=["hotel"])
app.include_router(booking_router, prefix="/booking", tags=["booking"])
app.include_router(room_router, prefix="/room", tags=["room"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(page_router, prefix="/page", tags=["page"])
app.include_router(image_router, prefix="/image", tags=["image"])

app.include_router(dev_router, prefix="/dev", tags=["dev"])

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
