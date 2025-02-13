import logging

import pytest
from httpx import AsyncClient

from src.database import async_session_factory
from src.users.service import UserService

@pytest.mark.asyncio
async def test_all_users(client: AsyncClient):
    response = await client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("example@example.com", "example", 200),
        ("example@example.com", "example", 409),
        ("example", "example", 422),
        ("1234455@example.com", "1234455", 200),
    ],
)

async def test_register_user(
    email: str, password: str, status_code: int, client: AsyncClient
) -> None:
    response = await client.post(
        "/users", json={"email": email, "password": password}
    )
    assert response.status_code == status_code


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "password", 200),
        ("artem@example.com", "password", 200),
        ("example", "example", 422),
        ("wrong@example.com", "1234455", 401),
    ],
)
async def test_login_user(
    email: str, password: str, status_code: int, client: AsyncClient
) -> None:
    response = await client.post(
        "/auth/token", json={"email": email, "password": password}
    )
    assert response.status_code == status_code


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "user_id, email, is_present",
    [
        (1, "test@test.com", True),
        (2, "artem@example.com", True),
        (3, "example@example.com", True),
        (999, "example@example.com", False),
    ],
)
async def test_find_user_by_id(user_id, email, is_present):
    async with async_session_factory() as session:
        user = await UserService.get_one_by_id(session, user_id)
        if is_present:
            assert user
            assert user.id == user_id
            assert user.email == email
        else:
            assert not user


@pytest.mark.asyncio
async def test_get_me(client: AsyncClient):
    response = await client.get("/auth/me")
    assert response.status_code == 401

    response = await client.post(
        "/auth/token", json={"email": "test@test.com", "password": "password"}
    )
    assert response.status_code == 200

    response = await client.get("/auth/me")
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"


@pytest.mark.asyncio
async def test_auth_get_me(authenticated_client: AsyncClient):
    response = await authenticated_client.get("/auth/me")
    assert response.status_code == 200
