import json
from datetime import datetime
from typing import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from src.bookings.models import Booking
from src.config import settings
from src.database import async_engine, async_session_factory
from src.hotels.models import Hotel
from src.models import Base
from src.rooms.models import Room
from src.users.models import User
from src.main import app as test_app


@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    if settings.MODE != "TEST":
        raise Exception

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def _open_mock_json(model: str) -> dict:
        mock_file = f"src/tests/mock_data/mock_{model}.json"
        with open(mock_file, "r", encoding="utf-8") as open_file:
            return json.load(open_file)

    hotels = _open_mock_json(model="hotels")
    rooms = _open_mock_json(model="rooms")
    users = _open_mock_json(model="users")
    bookings_ = _open_mock_json(model="bookings")

    for entry in users:
        entry['hashed_password'] = entry['hashed_password'].encode('utf-8')

    for d in bookings_:
        d["date_from"] = datetime.strptime(d["date_from"], "%Y-%m-%d")
        d["date_to"] = datetime.strptime(d["date_to"], "%Y-%m-%d")

    async with async_session_factory() as session:
        add_hotels = insert(Hotel).values(hotels)
        add_rooms = insert(Room).values(rooms)
        add_users = insert(User).values(users)
        add_bookings = insert(Booking).values(bookings_)

        await session.execute(add_hotels)
        await session.execute(add_rooms)
        await session.execute(add_users)
        await session.execute(add_bookings)

        await session.commit()


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create a http client."""
    async with AsyncClient(
        transport=ASGITransport(app=test_app),
        base_url="http://test",
    ) as ac:
        yield ac


@pytest_asyncio.fixture(scope="session")
async def authenticated_client() -> AsyncGenerator[AsyncClient, None]:
    """Create a http client."""
    async with AsyncClient(
        transport=ASGITransport(app=test_app),
        base_url="http://test",
    ) as ac:
        await ac.post(
            "/auth/token", json={"email": "test@test.com", "password": "password"}
        )
        yield ac
