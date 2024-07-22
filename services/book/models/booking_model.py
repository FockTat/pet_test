import json
from typing import List

from pydantic import BaseModel, field_validator, ValidationError


class Bookingdates(BaseModel):
    checkin: str
    checkout: str


class Booking(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: Bookingdates


class BookingModel(BaseModel):
    bookingid: int
    booking: Booking
    additionalneeds: str


# booking_json = {
#     "bookingid": 1,
#     "booking": {
#         "firstname": "Jim",
#         "lastname": "Brown",
#         "totalprice": 111,
#         "depositpaid": True,
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         }
#     },
#     "additionalneeds": "Breakfast"
# }
#
# try:
#     booking = BookingModel(**booking_json)
#     print(booking)
# except ValidationError as e:
#     print("ValidationError:", e.json())
