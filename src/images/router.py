import shutil

from fastapi import APIRouter, UploadFile

from src.config import settings
from src.tasks.tasks import process_image

image_router = APIRouter()


@image_router.post("/upload")
async def upload_file(name: int, file: UploadFile):
    image_path = f"{settings.IMAGE_PATH}/{name}.webp"
    with open(image_path, "wb+") as buffer:
        shutil.copyfileobj(file.file, buffer)

    process_image.delay(image_path)
    return {"message": "file uploaded"}
