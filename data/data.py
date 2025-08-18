import random

class TestData:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    # Existing test account (if needed)
    EXISTING_EMAIL = 'test_user_practikum_20@yandex.ru'
    EXISTING_PASSWORD = '123456'

    # Invalid credentials for negative tests
    INVALID_EMAIL = "wrong-email"
    INVALID_PASSWORD = "wrong-pass"

    # Example of dynamic test data (for order name etc.)
    PRODUCT_NAME = f"Test Product {random.randint(1000, 9999)}"

    @classmethod
    def url(cls, path: str):
        if not path.startswith('/'):
            path = '/' + path
        return cls.BASE_URL + path
    

    INGREDIENT_NAMES = [
        # Булки
        "Флюоресцентная булка R2-D3",
        "Краторная булка N-200i",
    ]

    CONSTRUCTOR = [
        # Булки
        "Флюоресцентная булка R2-D3",
        "Соус Spicy-X",
        "Соус фирменный Space Sauce",

        # Начинки
        "Мясо бессмертных моллюсков",
    ]

        
