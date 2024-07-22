from config.base_test import BaseTest


class TestBooking(BaseTest):

    def test_create_booking(self):
        booking = self.api_booking.create_booking()
        print(booking.lastname)