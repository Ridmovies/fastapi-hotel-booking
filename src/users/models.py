from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.bookings.models import Booking
from src.models import Base


class User(Base):
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[bytes]
    booking: Mapped[list["Booking"]] = relationship("Booking", back_populates="user")
