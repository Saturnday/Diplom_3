import pytest
import requests
from selenium import webdriver
from data.data import TestData
from helpers.generate_a_user import UserData


class UserAPI:

    @staticmethod
    def register_user(user_data):
        resp = requests.post(TestData.url("api/auth/register"), json=user_data)
        resp.raise_for_status()
        return resp

    @staticmethod
    def login_user(user_data):
        resp = requests.post(TestData.url("api/auth/login"), json=user_data)
        resp.raise_for_status()
        return resp.json()["accessToken"]

    @staticmethod
    def delete_user(access_token):
        requests.delete(
            TestData.url("api/auth/user"),
            headers={"Authorization": access_token}
        )


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        #options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-infobars")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        )
        driver = webdriver.Chrome(options=options)

        try:
            driver.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"}
            )
        except Exception:
            pass

    else:  # Firefox
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        options.set_preference(
            "general.useragent.override",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"
        )
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def test_user():
    user_data = UserData.generate_valid_user()
    UserAPI.register_user(user_data)
    access_token = UserAPI.login_user(user_data)

    yield {"user_data": user_data, "access_token": access_token}

    UserAPI.delete_user(access_token)


@pytest.fixture
def authorized_driver(driver, test_user):
    access_token = test_user["access_token"]

    driver.get(TestData.BASE_URL)
    driver.execute_script(f"""
        window.localStorage.setItem("accessToken", "{access_token}");
    """)
    driver.refresh()

    yield driver


@pytest.fixture(scope="session")
def existing_user_token():
    user_data = {
        "email": "new_user_20@yandex.com",
        "password": "1234567"
    }
    return UserAPI.login_user(user_data)

@pytest.fixture
def existing_user_driver(driver, existing_user_token):
    driver.get(TestData.BASE_URL)
    driver.execute_script(f"""
        window.localStorage.setItem("accessToken", "{existing_user_token}");
    """)
    driver.refresh()
    yield driver