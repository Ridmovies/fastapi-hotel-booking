from datetime import date
from operator import or_

from sqlalchemy import and_, func, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.bookings.models import Booking
from src.exceptions import RoomCantBookedException
from src.rooms.models import Room
from src.services import BaseService


class BookingService(BaseService):
    model = Booking

    @classmethod
    async def add_booking(
        cls,
        session: AsyncSession,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
    ):
        booked_rooms = (
            select(Booking)
            .where(
                and_(
                    Booking.room_id == room_id,
                    or_(
                        and_(
                            Booking.date_from >= date_from, Booking.date_from <= date_to
                        ),
                        and_(
                            Booking.date_from <= date_from, Booking.date_to > date_from
                        ),
                    ),
                )
            )
            .cte("booked_rooms")
        )

        get_available_rooms = (
            select(
                (Room.quantity - func.count(booked_rooms.c.room_id)).label(
                    "rooms_available"
                )
            )
            .select_from(Room)
            .join(booked_rooms, booked_rooms.c.room_id == Room.id, isouter=True)
            .where(Room.id == room_id)
            .group_by(Room.quantity, booked_rooms.c.room_id)
        )

        # print sql query to check if there are available rooms
        # print(get_available_rooms.compile(
        # bind=async_engine, compile_kwargs={"literal_binds": True})
        # )
        rooms_available = await session.execute(get_available_rooms)
        rooms_available = rooms_available.scalar()

        if not rooms_available:
            raise RoomCantBookedException

        get_room_price = select(Room.price_per_day).filter_by(id=room_id)

        price = await session.execute(get_room_price)
        price = price.scalar()

        add_booking = (
            insert(Booking)
            .values(
                user_id=user_id,
                room_id=room_id,
                date_from=date_from,
                date_to=date_to,
                price=price,
            )
            .returning(
                Booking.id,
                Booking.date_from,
                Booking.date_to,
                Booking.price,
                Booking.total_days,
                Booking.total_cost,
                Booking.room_id,
                Booking.user_id,
            )
        )

        new_booking = await session.execute(add_booking)
        await session.commit()
        return new_booking.mappings().one()
