from services.book.api_booking import BookingAPI


class BaseTest:

    def setup_method(self):
        self.api_booking = BookingAPI()
