from fastapi import HTTPException, status


class MyBookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(MyBookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User Already Exists."


class RoomCantBookedException(MyBookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "There are no rooms of this type left available."


class DateFromCannotBeAfterDateTo(MyBookingException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "The check-in date cannot be later than the check-out date."


class NotFoundException(MyBookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "No data found."
