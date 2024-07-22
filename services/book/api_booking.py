import allure
import requests
from utils.helper import Helper
from services.book.endpoints import Endpoints
from services.book.payload import Payloads
from config.headers import Headers
from services.book.models.booking_model import BookingModel


# super().__init__() позволяет расширить дочерний класс добавить какие-то атрибуты которых нет у родительских
# и наследовать при этом родительские методы
class BookingAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        # self.headers = Headers()

    @allure.step("Create booking")
    def create_booking(self):
        response = requests.post(
            url=self.endpoints.create_booking,
            # headers=self.headers.basic,
            json=self.payloads.create_booking
        )
        assert response.status_code == 200, response.json()
        self.attach_response(response.json())
        model = BookingModel(**response.json())
        return model
