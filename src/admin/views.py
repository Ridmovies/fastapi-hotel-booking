from sqladmin import ModelView

from src.bookings.models import Booking
from src.hotels.models import Hotel
from src.rooms.models import Room
from src.users.models import User


class UserAdmin(ModelView, model=User):
    """Класс для отображения пользователей в админке."""

    column_list = [User.id, User.email]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class BookingAdmin(ModelView, model=Booking):
    """Класс для отображения бронирований в админке."""

    column_labels = {"room.name": "room"}
    column_list = ["id", "user.email", "room.name"]
    name = "Бронирование"
    name_plural = "Бронирования"
    icon = "fa-solid fa-book"
    column_sortable_list = [
        "id",
        "user.email",
    ]


class HotelAdmin(ModelView, model=Hotel):
    """Класс для отображения отелей в админке."""

    column_list = "__all__"
    name = "Отель"
    name_plural = "Отели"
    icon = "fa-solid fa-hotel"
