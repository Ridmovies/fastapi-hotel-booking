from fastapi import APIRouter

from src.database import SessionDep
from src.users.schemas import UserSchemaCreate, UserSchemaBase, UserSchema
from src.users.service import UserService

user_router = APIRouter()


@user_router.get("/", response_model=list[UserSchema])
async def get_all_users(session: SessionDep):
    return await UserService.get_all(session)

@user_router.post("/", response_model=UserSchemaBase)
async def create_user(session: SessionDep, user_data: UserSchemaCreate):
    return await UserService.create(session, user_data)