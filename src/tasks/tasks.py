import smtplib
from pathlib import Path

from celery import Celery
from PIL import Image
from pydantic import EmailStr

from src.config import settings
from src.tasks.email_templates import create_booking_confirmation_template

celery = Celery("tasks", broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
celery.conf.broker_connection_retry_on_startup = True


@celery.task
def process_image(path: str):
    path_obj = Path(path)
    image = Image.open(path_obj)
    image_resize = image.resize((200, 200))
    new_path = f"{settings.IMAGE_RESIZED_PATH}/small_{path_obj.name}"
    image_resize.save(new_path)


@celery.task
def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
    """Отправляет email с подтверждением бронирования."""
    email_to = email_to
    email_content = create_booking_confirmation_template(
        booking=booking, email_to=email_to
    )
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(email_content)
