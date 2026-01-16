import pytest
import allure
from pages.main_page import MainPage
from locators.locators import MainPageLocators
from data.data import TestData


@allure.suite("Основной функционал (Main)")
class TestMain:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main = MainPage(driver)
        main.open()
        main.wait_for_page_ready()
        assert main.ingredient_found()

    @allure.title("Переход по клику на « Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main = MainPage(driver)
        main.open()
        main.click_order_feed_button()
        assert main.find_element_in_order_feed(MainPageLocators.FEED)

    @allure.title("Открытие/закрытие ингридиентов")
    @pytest.mark.parametrize("ingredient_name", TestData.INGREDIENT_NAMES)
    def test_open_and_close_one_ingredient_modal(self, driver, ingredient_name):
        main = MainPage(driver)
        main.open()

        ingredient_locator = MainPageLocators.ingredient_by_name(ingredient_name)
        main.click_to_element_with_wait(ingredient_locator)

        assert main.find_bun_details()

    @allure.title("Добавление ингредиента увеличивает каунтер")
    @pytest.mark.parametrize("ingredient_name", TestData.CONSTRUCTOR)
    def test_add_ingredient_increases_counter(self, driver, ingredient_name):
        main = MainPage(driver)
        main.open()

        before = main.get_order_counter(ingredient_name)
        
        main.add_ingredient_to_constructor(ingredient_name)
        
        main.wait_for_counter_change(ingredient_name, before)
        after = main.get_order_counter(ingredient_name)

        assert int(after) > int(before)

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_order(self, existing_user_driver):
        driver = existing_user_driver

        main = MainPage(driver)
        main.open()
        main.create_an_order()

        assert main.order_in_process()
        
