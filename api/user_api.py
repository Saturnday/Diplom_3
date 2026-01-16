import requests
from data.data import TestData

class UserAPI:
    BASE_URL = TestData.BASE_URL

    @classmethod
    def _url(cls, path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return cls.BASE_URL + path

    @classmethod
    def register_user(cls, user_data: dict):
        resp = requests.post(cls._url("api/auth/register"), json=user_data)
        resp.raise_for_status()
        return resp.json()

    @classmethod
    def login_user(cls, user_data: dict) -> str:
        resp = requests.post(cls._url("api/auth/login"), json=user_data)
        resp.raise_for_status()
        return resp.json()["accessToken"]

    @classmethod
    def delete_user(cls, access_token: str):
        requests.delete(
            cls._url("api/auth/user"),
            headers={"Authorization": access_token}
        )
