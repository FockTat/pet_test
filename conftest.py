import requests
import pytest

HOST = 'https://restful-booker.herokuapp.com'


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f'{HOST}/booking'
    )
    assert response.status_code == 200
