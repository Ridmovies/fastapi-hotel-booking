from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """create __tablename__ table name"""
        return f"{cls.__name__.lower()}"


    id: Mapped[int] = mapped_column(primary_key=True)