from fastapi import APIRouter

from src.database import SessionDep
from src.hotels.service import HotelService

hotel_router = APIRouter()


@hotel_router.get("")
async def get_all_hotels(session: SessionDep):
    """Get all hotels"""
    return await HotelService.get_all(session)