from faker import Faker

fake = Faker()


class Payloads:
    create_booking = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_number(),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": fake.date(),
            "checkout": fake.date()
        },
        "additionalneeds": fake.text(12)
    }


