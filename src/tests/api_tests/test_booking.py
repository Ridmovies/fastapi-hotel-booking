import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_booking(authenticated_client: AsyncClient):
    response = await authenticated_client.get("/booking")
    assert response.status_code == 200
    assert len(response.json()) == 3

@pytest.mark.asyncio
async def test_get_my_booking(authenticated_client: AsyncClient):
    response = await authenticated_client.get("/booking/my")
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.asyncio
async def test_post_booking_unauthorized(client: AsyncClient):
    response = await client.get("/booking/my")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_post_booking(authenticated_client: AsyncClient):
    response = await authenticated_client.post(
        "/booking",
        params={
            "room_id": 1,
            "date_from": "2025-02-14",
            "date_to": "2025-02-21",
        },
    )
    assert response.status_code == 200
    assert response.json()["room_id"] == 1
    assert response.json()["id"] == 4

    response = await authenticated_client.get("/booking/my")
    assert response.status_code == 200
    assert len(response.json()) == 3


@pytest.mark.asyncio
async def test_post_booking_not_available(authenticated_client: AsyncClient):
    params = {
        "room_id": 1,
        "date_from": "2025-02-14",
        "date_to": "2025-02-21",
    }
    response = await authenticated_client.post("/booking", params=params)
    assert response.status_code == 200
    response = await authenticated_client.post("/booking", params=params)
    assert response.status_code == 409
    assert response.json() == {"detail": "There are no rooms of this type left available."}




