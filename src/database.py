from typing import Annotated, AsyncGenerator

from fastapi import Depends
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from src.config import settings


if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DATABASE_URL
    # to fix RuntimeError: Task <Task pending name='Task-4'
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DATABASE_URL
    DATABASE_PARAMS = {}

async_engine = create_async_engine(DATABASE_URL, echo=False, **DATABASE_PARAMS)

async_session_factory = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
