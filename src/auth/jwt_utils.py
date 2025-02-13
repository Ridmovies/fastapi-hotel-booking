from datetime import timedelta, datetime, timezone
from typing import Annotated

import jwt
from fastapi import Depends, Request, Response
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.exception import credentials_exception
from src.auth.pwd_utils import verify_password
from src.auth.schemas import TokenData
from src.config import settings
from src.database import async_session_factory
from src.users.models import User
from src.users.service import UserService


SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


async def authenticate_user(session: AsyncSession, email: str, password: str):
    user: User = await UserService.get_one_or_none(session=session, email=email)
    if not user:
        raise credentials_exception
    if not verify_password(password, user.hashed_password):
        raise credentials_exception
    return user

async def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_user_by_email(email: str) -> User:
    async with async_session_factory() as session:
        user: User = await UserService.get_one_or_none(session=session, email=email)
        if not user:
            raise credentials_exception
        return user


def get_access_token(request: Request):
    """This function is used to get the access token for cookie transport"""
    access_token = request.cookies.get("access_token")
    print(f"{access_token=}")
    if not access_token:
        raise credentials_exception
    return access_token


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)]
        if settings.JWT_TRANSPORT == "BEARER"
        else Annotated[str, Depends(get_access_token)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user: User = await get_user_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


UserDep = Annotated[User, Depends(get_current_user)]