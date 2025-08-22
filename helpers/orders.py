import allure
import requests
from data.data import TestData
from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.nomoreparties.site/api"

allure.story('API')
class ApiMethods:
    @allure.step('получить ингридиенты')
    def get_ingredient_ids():
        
        resp = requests.get(f"{BASE_URL}/ingredients")
        resp.raise_for_status()

        data = resp.json()
        if not data.get("success"):
            raise ValueError(f"Ошибка при получении ингредиентов: {data}")

        return [item["_id"] for item in data["data"]]

    @allure.step('создать заказ через АПИ')
    def create_order_via_api(ingredient_ids, token=None):

        headers = {"Authorization": token} if token else {}
        payload = {"ingredients": ingredient_ids}
        resp = requests.post(TestData.url("api/orders"), headers=headers, json=payload)
        resp.raise_for_status()
        data = resp.json()

        if not data.get("success"):
            raise ValueError(f"Ошибка при создании заказа: {data}")

        return data["order"]["number"]
    
@allure.story('Locators')
class GetLocators:

    @staticmethod
    def ingredient_by_name(name):
        return By.XPATH, f"//p[contains(text(), '{name}')]"
    
    @staticmethod
    def element_to():
        return (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда')]")
    




