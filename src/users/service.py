from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.pwd_utils import get_password_hash
from src.services import BaseService
from src.users.models import User
from src.users.schemas import UserSchemaCreate


class UserService(BaseService):
    model = User

    @classmethod
    async def create_user(
            cls, session: AsyncSession, user_data: UserSchemaCreate
    ) -> User | None:
        user_data_dict: dict = user_data.model_dump()
        email: str | None = user_data_dict.get("email")
        password: str | None = user_data_dict.get("password")
        if not isinstance(password, str):
            raise ValueError("Password must be a string.")
        hashed_password: bytes = get_password_hash(password)
        user: User = User(email=email, hashed_password=hashed_password)
        session.add(user)
        await session.commit()
        return user
