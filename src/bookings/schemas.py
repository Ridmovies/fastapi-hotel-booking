from datetime import date

from pydantic import BaseModel


class BookingBase(BaseModel):
    date_from: date
    date_to: date
    price: int
    room_id: int


class BookingCreate(BookingBase):
    pass

class BookingSchema(BookingBase):
    id: int
    total_cost: int
    total_days: int
    user_id: int
