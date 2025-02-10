from fastapi import APIRouter

from src.database import SessionDep
from src.rooms.service import RoomService

room_router = APIRouter()


@room_router.get("")
async def get_all_rooms(session: SessionDep):
    """Get all rooms"""
    return await RoomService.get_all(session)