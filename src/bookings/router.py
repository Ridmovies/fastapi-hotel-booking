from datetime import date

from fastapi import APIRouter
from pydantic import TypeAdapter

from src.auth.jwt_utils import UserDep
from src.bookings.schemas import BookingSchema
from src.bookings.service import BookingService
from src.config import settings
from src.database import SessionDep

from src.tasks.tasks import send_booking_confirmation_email

booking_router = APIRouter()


@booking_router.get("", response_model=list[BookingSchema])
async def get_all_bookings(session: SessionDep):
    """Get all bookings"""
    return await BookingService.get_all(session)


@booking_router.get("/my", response_model=list[BookingSchema])
async def get_my_bookings(session: SessionDep, user: UserDep):
    """Get all my bookings"""
    return await BookingService.get_all(session, user_id=user.id)


@booking_router.post("", response_model=BookingSchema)
async def create_booking(
    session: SessionDep, user: UserDep, room_id: int, date_from: date, date_to: date
):
    """Create a new booking"""
    booking = await BookingService.add_booking(
        session=session,
        user_id=user.id,
        room_id=room_id,
        date_from=date_from,
        date_to=date_to,
    )
    # Создаем адаптер для вашего типа данных
    adapter = TypeAdapter(BookingSchema)

    booking_dict = adapter.validate_python(booking).model_dump()
    # turn_on_email_notification
    if settings.turn_on_email_notification:
        send_booking_confirmation_email.delay(booking=booking_dict, email_to=user.email)
    return booking_dict
