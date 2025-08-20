import pytest
import allure
import requests
from selenium import webdriver
from helpers.generate_a_user import UserData



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


class UserAPI:
    @staticmethod
    @allure.step("Регистрация пользователя через API")
    def register_user(user_data, base_url):
        url = f"{base_url}/api/auth/register"
        payload = {
            "email": user_data.email,
            "password": user_data.password,
            "name": user_data.name
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()


@pytest.fixture
def new_user(base_url):
    """Создание и регистрация нового пользователя через API"""
    user = UserData()
    UserAPI.register_user(user, base_url)
    return user