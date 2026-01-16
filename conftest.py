import pytest
import requests
from selenium import webdriver
from helpers.generate_a_user import UserData
from api.user_api import UserAPI

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
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


@pytest.fixture
def new_user():
    """Создание и регистрация нового пользователя через API"""
    user = UserData().as_dict()   # make sure UserData can give dict
    UserAPI.register_user(user)
    return user

@pytest.fixture(scope="session")
def existing_user_token():
    user_data = {
        "email": "new_user_20@yandex.com",
        "password": "1234567"
    }
    return UserAPI.login_user(user_data)

@pytest.fixture
def existing_user_driver(driver, existing_user_token):
    driver.get('https://stellarburgers.nomoreparties.site')
    driver.execute_script(
        f'window.localStorage.setItem("accessToken", "{existing_user_token}");'
    )
    driver.refresh()
    yield driver