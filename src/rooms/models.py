from typing import Optional

from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base



class Room(Base):
    name: Mapped[str] = mapped_column(String(length=150), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(
        String(length=500), nullable=True
    )
    price_per_day: Mapped[int]
    services: Mapped[str] = mapped_column(JSON, nullable=False)
    quantity: Mapped[int]
    image_id: Mapped[int]
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotel.id"))
    # hotel: Mapped["Hotel"] = relationship("Hotel", back_populates="rooms")
    # booking: Mapped[list["Booking"]] = relationship("Booking", back_populates="room")

    def __str__(self):
        return f"room: id - {self.id}, name - {self.name}"
