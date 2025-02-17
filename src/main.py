from contextlib import asynccontextmanager
import time
import sentry_sdk
from typing import AsyncIterator

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_versioning import VersionedFastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from redis import asyncio as aioredis
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware

from src.admin.auth import authentication_backend
from src.admin.views import BookingAdmin, HotelAdmin, UserAdmin
from src.auth.router import auth_router
from src.bookings.router import booking_router
from src.database import async_engine
from src.dev.router import dev_router
from src.hotels.router import hotel_router
from src.images.router import image_router
from src.logger import logger
from src.pages.router import page_router
from src.rooms.router import room_router
from src.users.router import user_router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(
    title='Booking API',
    lifespan=lifespan,
)

origins = [
    "http://localhost:3000",
]


sentry_sdk.init(
    dsn="https://a89d03b408ba6a73d6094b8b22f4e395@o4506981955272704.ingest.us.sentry.io/4508822225289216",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    _experiments={
        # Set continuous_profiling_auto_start to True
        # to automatically start the profiler on when
        # possible.
        "continuous_profiling_auto_start": True,
    },
)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(hotel_router, prefix="/hotel", tags=["hotel"])
app.include_router(booking_router, prefix="/booking", tags=["booking"])
app.include_router(room_router, prefix="/room", tags=["room"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(page_router, prefix="/page", tags=["page"])
app.include_router(image_router, prefix="/image", tags=["image"])

app.include_router(dev_router, prefix="/dev", tags=["dev"])

# Place above all mounts, but after all routers. Location is important.
app = VersionedFastAPI(
    app,
    version_format="{major}",
    prefix_format="/v{major}",
    description="Booking API Description",
)


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


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """Добавляет заголовок со временем выполнения запроса."""
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Request handling time",
                extra={
                    "request_to": request.url,
                    "method": request.method,
                    "process_time": round(process_time, 4)
                })
    return response



instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"],
)
instrumentator.instrument(app).expose(app)


app.mount("/static", StaticFiles(directory="src/static"), name="static")
admin = Admin(app, async_engine, authentication_backend=authentication_backend)
admin.add_view(UserAdmin)
admin.add_view(BookingAdmin)
admin.add_view(HotelAdmin)