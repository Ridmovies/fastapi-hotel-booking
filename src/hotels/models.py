from sqlalchemy.orm import Mapped

from src.models import Base


class Hotel(Base):
    name: Mapped[str]
    location: Mapped[str]
    # services: Mapped[str]
    # rooms_quantity: Mapped[int]
    # image_id: Mapped[int]
    # rooms: Mapped[list["Room"]] = relationship("Room", back_populates="hotel")