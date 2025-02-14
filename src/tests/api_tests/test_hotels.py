import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_hotels(client: AsyncClient):
    response = await client.get("/hotel")
    assert response.status_code == 200
    assert len(response.json()) == 6


@pytest.mark.asyncio
async def test_get_hotel_by_location(client: AsyncClient):
    location = "Алтай"
    params = {
        "date_from": "2025-02-14",
        "date_to": "2025-02-21",
    }
    response = await client.get(f"/hotel/{location}", params=params)
    assert response.status_code == 200
    assert len(response.json()) == 3
