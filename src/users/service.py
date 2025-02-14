from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.pwd_utils import get_password_hash
from src.services import BaseService
from src.users.models import User
from src.users.schemas import UserSchemaCreate


class UserService(BaseService):
    model = User

    @classmethod
    async def create_user(cls, session: AsyncSession, user_data: UserSchemaCreate):
        user_data_dict: dict = user_data.model_dump()
        email: str = user_data_dict.get("email")
        password: str = user_data_dict.get("password")
        hashed_password: bytes = get_password_hash(password)
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        await session.commit()
        return user
