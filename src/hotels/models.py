from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, relationship

from src.models import Base
from src.rooms.models import Room


class Hotel(Base):
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[str]
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]
    rooms: Mapped[list["Room"]] = relationship("Room", back_populates="hotel")
