from src.bookings.models import Booking
from src.services import BaseService

class BookingService(BaseService):
    model = Booking