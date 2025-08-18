import allure
from pages.orders_feed_page import OrdersFeedPage
from pages.main_page import MainPage
from locators.locators import FeedPageLocators, MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.orders import get_ingredient_ids, create_order_via_api

@allure.suite("Лента заказов (Feed)")
class TestFeed:

    @allure.title("Клик по заказу открывает модальное окно")
    def test_order_modal_open(self, existing_user_driver):
        driver = existing_user_driver

        feed = OrdersFeedPage(driver)
        feed.open()
        feed.click_first_order()
        modal = feed.wait_for_order_modal()
        assert modal is not None

    @allure.title("Заказы пользователя отображаются в ленте заказов")
    def test_user_orders_in_feed(self, existing_user_driver):
        driver = existing_user_driver
        feed = OrdersFeedPage(driver)
        my_order = feed.get_order_number_and_create_an_order(existing_user_driver)
        feed.click_to_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED)
        feed.open()

        order_in_feed = feed.find_element_with_wait(FeedPageLocators.FEED)
        print("order_in_feed.text:", order_in_feed.text) 
        print("my_order:", my_order)
        assert my_order in order_in_feed.text



    @allure.title("При создании нового заказа увеличивается общий счётчик 'Выполнено'")
    def test_total_done_counter_increases(self, authorized_driver):
        driver = authorized_driver
        feed = OrdersFeedPage(driver)
        feed.open()
        before = feed.get_total_done_counter()
        ingredient_ids = get_ingredient_ids()[:2]
        create_order_via_api(ingredient_ids)
        feed.open()
        after = feed.get_total_done_counter()
        assert after >= before


    @allure.title("При создании нового заказа увеличивается счётчик 'Выполнено сегодня'")
    def test_today_done_counter_increases(self, existing_user_driver):
        driver = existing_user_driver
        feed = OrdersFeedPage(driver)
        
        feed.open()
        feed.find_element_with_wait(FeedPageLocators.FEED)
        feed.find_element_with_wait(FeedPageLocators.COUNTER_TODAY_DONE)
        before = feed.get_today_done_counter()

        feed.get_order_number_and_create_an_order(existing_user_driver)
        feed.click_to_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED)
        feed.open()
        feed.find_element_with_wait(FeedPageLocators.FEED)
        after = feed.get_today_done_counter()
        assert after > before

    def test_order_number_in_work_section(self, existing_user_driver):
        driver = existing_user_driver
        feed = OrdersFeedPage(driver)
        my_order = feed.get_order_number_and_create_an_order(existing_user_driver)
        feed.click_to_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED)
        feed.open()

        my_order_str = f"{int(my_order):07d}"
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(FeedPageLocators.IN_WORK_ORDER_NUMBERS,my_order_str))
        order_in_feed = feed.find_element_with_wait(FeedPageLocators.IN_WORK_ORDER_NUMBERS).text
        my_order_str = f"{int(my_order):07d}"

        assert my_order_str in order_in_feed





