from datetime import date

from sqlalchemy import select, func, or_, and_
from sqlalchemy.ext.asyncio import AsyncSession

from src.bookings.models import Booking
from src.hotels.models import Hotel
from src.rooms.models import Room
from src.services import BaseService

class HotelService(BaseService):
    model = Hotel

    @classmethod
    async def get_hotels_by_location_objects(
            cls,
            session: AsyncSession,
            location: str,
            date_from: date,
            date_to: date
    ):
        """Возвращает все отели по заданным параметрам местоположения
        и времени."""
        booked_rooms = (
            select(Booking.room_id, func.count(Booking.room_id)
                   .label('count_booked_rooms'))
            .select_from(Booking)
            .where(
                or_(
                    and_(
                        Booking.date_from >= date_from,
                        Booking.date_from <= date_to,
                    ),
                    and_(
                        Booking.date_from <= date_from,
                        Booking.date_to > date_from,
                    ),
                ),
            )
            .group_by(Booking.room_id)
            .cte('booked_rooms')
        )

        booked_hotels = (
            select(
                Room.hotel_id,
                func.sum(Room.quantity - func.coalesce(booked_rooms.c.count_booked_rooms, 0))
                .label('available_rooms')
            )
            .select_from(Room)
            .join(
                booked_rooms,
                booked_rooms.c.room_id == Room.id,
                isouter=True
            )
            .group_by(Room.hotel_id)
            .cte('booked_hotels')
        )

        hotels_with_rooms = (
            select(
                Hotel.__table__.columns,
                booked_hotels.c.available_rooms
            )
            .join(
                booked_hotels,
                booked_hotels.c.hotel_id == Hotel.id,
                isouter=True
            )
            .where(
                and_(
                    booked_hotels.c.available_rooms > 0,
                    Hotel.location.like(f'%{location}%'),
                )
            )
        )

        hotels_with_rooms = await session.execute(hotels_with_rooms)
        return hotels_with_rooms.mappings().all()

    @classmethod
    async def get_all_hotel_rooms_objects(
            cls,
            session: AsyncSession,
            hotel_id: int,
            date_from: date, date_to: date
    ):
        """Возвращает список всех/доступных номеров определенного отеля
        на конкретный промежуток времени."""
        booked_rooms = (
            select(Booking.room_id, func.count(Booking.room_id)
                   .label('count_booked_rooms'))
            .select_from(Booking)
            .where(
                or_(
                    and_(
                        Booking.date_from >= date_from,
                        Booking.date_from <= date_to,
                    ),
                    and_(
                        Booking.date_from <= date_from,
                        Booking.date_to > date_from,
                    ),
                ),
            )
            .group_by(Booking.room_id)
            .cte('booked_rooms')
        )

        get_rooms = (
            select(
                Room.__table__.columns,
                (Room.quantity - func.coalesce(booked_rooms.c.count_booked_rooms, 0))
                .label('available_rooms'),
                (Room.price_per_day * (date_to - date_from).days)
                .label('preliminary_cost')
            )
            .join(
                booked_rooms,
                booked_rooms.c.room_id == Room.id,
                isouter=True)
            .where(
                Room.hotel_id == hotel_id
            )
        )


        all_hotels_rooms = await session.execute(get_rooms)
        return all_hotels_rooms.mappings().all()