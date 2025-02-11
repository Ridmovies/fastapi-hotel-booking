from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from src.hotels.router import get_hotels_by_location

page_router = APIRouter()


templates = Jinja2Templates(directory="src/templates")


@page_router.get("/hotels")
async def get_hotels_page(
    request: Request,
    hotels=Depends(get_hotels_by_location),
):
    return templates.TemplateResponse(
        name="hotels.html",
        context={"request": request, "hotels": hotels},
    )



