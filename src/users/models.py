from sqlalchemy.orm import Mapped

from src.models import Base


class User(Base):
    hashed_password: Mapped[str]
    email: Mapped[str | None]