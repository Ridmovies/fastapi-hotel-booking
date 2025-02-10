from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.auth.exception import credentials_exception
from src.auth.jwt_utils import authenticate_user, create_access_token, get_current_user
from src.auth.schemas import TokenSchema
from src.config import settings
from src.database import SessionDep
from src.users.models import User
from src.users.schemas import UserSchema

ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter()

@auth_router.post("/token")
async def login_for_access_token(
        session: SessionDep,
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],

) -> TokenSchema:
    user = await authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise credentials_exception
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return TokenSchema(access_token=access_token)


@auth_router.get("/me", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user