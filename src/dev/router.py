import time
from random import random

from fastapi import APIRouter, Request, Response
from fastapi_versioning import version
from sqlalchemy import text

from src.database import SessionDep, async_engine
from src.models import Base

dev_router = APIRouter()


@dev_router.get("/check-db-connection")
@version(2)
async def check_db_connection(session: SessionDep):
    """Check if the database connection is successful"""
    await session.execute(text("SELECT 1"))
    return {"message": "Connection to the database successful"}


@dev_router.post("/create_db_tables")
async def create_db_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return {"message": "Database tables created"}


@dev_router.post("/set_cookie")
@version(2)
async def set_cookie(response: Response):
    """Set a cookie"""
    response.set_cookie(key="123", value="value", httponly=True)
    return {"message": "Cookie set"}


@dev_router.post("/delete_cookie")
@version(2)
async def delete_cookie(response: Response):
    """Delete a cookie"""
    response.delete_cookie(key="123", httponly=True)
    return {"message": "Cookie deleted"}


@dev_router.get("/get_cookie")
@version(2)
async def get_cookie(request: Request):
    """Get a cookie"""
    cookie = request.cookies.get("123")
    return {"cookie": cookie}


@dev_router.get("/sentry-debug")
@version(2)
async def trigger_error():
    """Trigger an error"""
    division_by_zero = 1 / 0


@dev_router.get("/prometheus/get_error")
@version(1)
def get_error():
    """Функция для теста Prometheus + Grafana."""
    if random() > 0.5:
        raise ZeroDivisionError
    else:
        raise KeyError


@dev_router.get("/prometheus/time_consumer")
@version(1)
def time_consumer():
    """Функция для теста Prometheus + Grafana."""
    time.sleep(random() * 5)
    return "Тест завершен."


@dev_router.get("/prometheus/memory_consumer")
@version(1)
def memory_consumer():
    """Функция для теста Prometheus + Grafana."""
    _ = [i for i in range(30_000_000)]
    return "Тест завершен."