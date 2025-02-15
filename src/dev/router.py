from fastapi import APIRouter, Request, Response
from fastapi_versioning import version
from sqlalchemy import text

from src.database import SessionDep

dev_router = APIRouter()


@dev_router.get("/check-db-connection")
@version(2)
async def check_db_connection(session: SessionDep):
    """Check if the database connection is successful"""
    await session.execute(text("SELECT 1"))
    return {"message": "Connection to the database successful"}


@dev_router.post("/set_cookie")
@version(2)
async def set_cookie(response: Response):
    """Set a cookie"""
    response.set_cookie(key="123", value="value", httponly=True)
    return {"message": "Cookie set"}


@dev_router.post("/delete_cookie")
@version(2)
async def delete_cookie(response: Response):
    """Delete a cookie"""
    response.delete_cookie(key="123", httponly=True)
    return {"message": "Cookie deleted"}


@dev_router.get("/get_cookie")
@version(2)
async def get_cookie(request: Request):
    """Get a cookie"""
    cookie = request.cookies.get("123")
    return {"cookie": cookie}


@dev_router.get("/sentry-debug")
@version(2)
async def trigger_error():
    """Trigger an error"""
    division_by_zero = 1 / 0