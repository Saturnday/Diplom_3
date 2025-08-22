from pages.base_page import BasePage
from pages.main_page import MainPage
from data.data import TestData
from locators.locators import FeedPageLocators, MainPageLocators
import allure


class OrdersFeedPage(BasePage):
    URL = TestData.BASE_URL + "/feed"

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        self.open_url(self.URL)
        self.wait_for_page_ready()

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.click_to_element_with_wait(FeedPageLocators.FEED_ORDER_ITEM)

    @allure.step("Ждать открытия модального окна заказа")
    def wait_for_order_modal(self):
        return self.find_element_with_wait(FeedPageLocators.FEED_ORDER_MODAL)

    @allure.step("Получить все номера заказов из ленты")
    def get_all_order_numbers_on_feed(self):
        els = self.find_elements_with_wait(FeedPageLocators.ALL_ORDER_NUMBERS)
        return [e.text.strip() for e in els]

    @allure.step("Получить общий счётчик выполненных заказов")
    def get_total_done_counter(self):
        try:
            txt = self.find_element_with_wait(FeedPageLocators.COUNTER_TOTAL_DONE).text
            return int(''.join(filter(str.isdigit, txt)) or 0)
        except Exception:
            return 0

    @allure.step("Получить счётчик заказов за сегодня")
    def get_today_done_counter(self):
        return int(self.find_element_with_wait(FeedPageLocators.COUNTER_TODAY_DONE, timeout=15).text)

    @allure.step("Получить номера заказов в работе")
    def get_in_work_order_numbers(self):
        els = self.find_elements_with_wait(FeedPageLocators.IN_WORK_ORDER_NUMBERS, timeout=15)
        return [e.text.strip() for e in els]
    
    @allure.step("Перейти в ленту заказов")
    def click_to_feed(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step("Проверить наличие заказа {my_order} в ленте")
    def find_order_in_feed(self, my_order):
        order_in_feed = self.find_element_with_wait(FeedPageLocators.FEED)
        return my_order in order_in_feed.text
    
    @allure.step("Открыть ленту и дождаться загрузки счётчиков")
    def open_feed_load_counters(self):
            self.open()
            self.find_element_with_wait(FeedPageLocators.FEED)
            self.find_element_with_wait(FeedPageLocators.COUNTER_TODAY_DONE)

    @allure.step("Проверить, что заказ {my_order} появился в списке заказов в работе")
    def my_order_in_order_in_feed(self, my_order):
        my_order_str = f"{int(my_order):07d}"
        order_in_feed = self.find_element_with_text(FeedPageLocators.IN_WORK_ORDER_NUMBERS, my_order_str)
        return (my_order in order_in_feed)

    
        


