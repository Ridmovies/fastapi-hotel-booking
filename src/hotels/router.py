from datetime import date, datetime, timedelta

from fastapi import APIRouter, Query

from src.bookings.service import BookingService
from src.database import SessionDep
from src.exceptions import DateFromCannotBeAfterDateTo, NotFoundException
from src.hotels.service import HotelService

hotel_router = APIRouter()


@hotel_router.get("")
async def get_all_hotels(session: SessionDep):
    """Get all hotels"""
    return await HotelService.get_all(session)


@hotel_router.get('/{location}')
async def get_hotels_by_location(
    session: SessionDep,
    location: str,
    date_from: date = Query(
        ..., description=f'Например, {datetime.now().date()}'
    ),
    date_to: date = Query(
        ..., description=f'Например, {(datetime.now() + timedelta(days=7)).date()}'
    ),
):
    """Возвращает все отели по заданным параметрам местоположения."""
    if date_from > date_to:
        raise DateFromCannotBeAfterDateTo
    hotels = await HotelService.get_hotels_by_location_objects(
        session=session, location=location, date_from=date_from, date_to=date_to
    )


    if not hotels:
        raise NotFoundException
    return hotels