from sqladmin.authentication import AuthenticationBackend
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request

from src.auth.jwt_utils import authenticate_user, create_access_token, get_current_user
from src.database import get_session, SessionDep, async_session_factory


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        async with async_session_factory() as session:
            user = await authenticate_user(session, email, password)
            if user:
                access_token = await create_access_token({"sub": email})
                request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        user = await get_current_user(token)
        if not user:
            return False
        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="...")
