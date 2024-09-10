from calendar import month, month_abbr

from faker import Faker
from faker.contrib.pytest.plugin import faker
from faker.providers import DynamicProvider

class RandomUser:
    fake = Faker()

    @classmethod
    def generate_name(cls):
        return cls.fake.first_name()

    @classmethod
    def generate_email(cls):
        return cls.fake.email()

    @classmethod
    def generate_password(cls):
        return cls.fake.password()

    @classmethod
    def generate_first_name(cls):
        return cls.fake.first_name()

    @classmethod
    def generate_last_name(cls):
        return cls.fake.last_name()

    @classmethod
    def generate_company_name(cls):
        return cls.fake.company()

    @classmethod
    def generate_address(cls):
        return cls.fake.address()

    @classmethod
    def generate_address_details(cls):
        return cls.fake.address()

    @classmethod
    def generate_state(cls):
        return cls.fake.state()

    @classmethod
    def generate_city(cls):
        return cls.fake.city()

    @classmethod
    def generate_zipcode(cls):
        return cls.fake.zipcode()

    @classmethod
    def generate_phone_number(cls):
        return cls.fake.phone_number()

class RandomMessage:
    fake = Faker()

    @classmethod
    def generate_subject(cls):
        return cls.fake.sentence()
    @classmethod
    def generate_message(cls):
        return cls.fake.text()

class RandomCardDetails:
    fake = Faker()

    @classmethod
    def generate_card_number(cls):
        return cls.fake.credit_card_number()

    @classmethod
    def generate_cvc(cls):
        return cls.fake.credit_card_security_code()

class RandomProductName:
    product_name_provider = DynamicProvider(
        provider_name='product_name',
        elements=["Blue Top",
                  "Men Tshirt",
                  "Sleeveless Dress",
                  "Stylish Dress",
                  "Winter Top",
                  "Summer White Top",
                  "Fancy Green Top"],
    )
    fake = Faker()
    fake.add_provider(product_name_provider)

    @classmethod
    def generate_search_word(cls):
        return cls.fake.product_name()