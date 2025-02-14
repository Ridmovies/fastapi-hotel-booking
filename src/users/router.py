from fastapi import APIRouter

from src.database import SessionDep
from src.exceptions import UserAlreadyExistsException
from src.users.schemas import UserSchema, UserSchemaCreate
from src.users.service import UserService

user_router = APIRouter()


@user_router.get("", response_model=list[UserSchema])
async def get_all_users(session: SessionDep):
    return await UserService.get_all(session)


@user_router.post("", response_model=UserSchema)
async def create_user(session: SessionDep, user_data: UserSchemaCreate):
    exist_user = await UserService.get_one_or_none(
        session=session, email=user_data.email
    )
    if exist_user:
        raise UserAlreadyExistsException
    return await UserService.create_user(session, user_data)
