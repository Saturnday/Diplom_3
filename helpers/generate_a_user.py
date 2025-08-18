import random

class UserData:
    
    @staticmethod
    def generate_valid_user():
        return {
            "email": f"test{random.randint(1000, 9999)}@mail.ru",
            "password": "password123",
            "name": "TestUser"
        }