from fastapi import APIRouter

from src.bookings.service import BookingService
from src.database import SessionDep

booking_router = APIRouter()


@booking_router.get("")
async def get_all_bookings(session: SessionDep):
    """Get all bookings"""
    return await BookingService.get_all(session)