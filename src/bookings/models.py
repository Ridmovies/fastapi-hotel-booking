from sqlalchemy import ForeignKey, Date, Computed
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class Booking(Base):
    date_from: Mapped[Date]
    date_to: Mapped[Date]
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from + 1) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from + 1"))

    room_id: Mapped[int] = mapped_column(ForeignKey("room.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
