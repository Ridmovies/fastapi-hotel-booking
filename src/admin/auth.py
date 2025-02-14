from fastapi import UploadFile
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.auth.jwt_utils import authenticate_user, create_access_token, get_current_user
from src.database import async_session_factory
from src.users.models import User


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email: UploadFile | str | None = form.get("username")
        password: UploadFile | str | None = form.get("password")
        async with async_session_factory() as session:
            if isinstance(email, str) and isinstance(password, str):
                user: User | None = await authenticate_user(session, email, password)
                if user:
                    access_token = await create_access_token({"sub": email})
                    request.session.update({"token": access_token})
                    return True
        return False

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
        return True


authentication_backend = AdminAuth(secret_key="...")
