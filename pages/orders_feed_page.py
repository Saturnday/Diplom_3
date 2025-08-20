from pages.base_page import BasePage
from pages.main_page import MainPage
from data.data import TestData
from locators.locators import FeedPageLocators, MainPageLocators


class OrdersFeedPage(BasePage):
    URL = TestData.BASE_URL + "/feed"

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_ready()

    def click_first_order(self):
        self.click_to_element_with_wait(FeedPageLocators.FEED_ORDER_ITEM)

    def wait_for_order_modal(self):
        return self.find_element_with_wait(FeedPageLocators.FEED_ORDER_MODAL)

    def get_all_order_numbers_on_feed(self):
        els = self.driver.find_elements(*FeedPageLocators.ALL_ORDER_NUMBERS)
        return [e.text.strip() for e in els]

    def get_total_done_counter(self):
        try:
            txt = self.find_element_with_wait(FeedPageLocators.COUNTER_TOTAL_DONE).text
            return int(''.join(filter(str.isdigit, txt)) or 0)
        except Exception:
            return 0

    def get_today_done_counter(self):
        return int(self.find_element_with_wait(FeedPageLocators.COUNTER_TODAY_DONE, timeout=15).text)

    def get_in_work_order_numbers(self):
        els = self.find_elements_with_wait(FeedPageLocators.IN_WORK_ORDER_NUMBERS, timeout=15)
        return [e.text.strip() for e in els]
    

    def get_order_number_and_create_an_order(self, existing_user_driver):
        driver = existing_user_driver
        main = MainPage(driver)
        main.open()
        main.click_to_element_with_wait(MainPageLocators.LOGIN)
        main.add_ingredient_to_constructor(TestData.CONSTRUCTOR[0])
        main.click_to_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)
        main.wait_until_order_number_is_real(MainPageLocators.ORDER_NUMBER, '9999')
        order_number_el = self.find_element_with_wait(MainPageLocators.ORDER_NUMBER)
        order_number = order_number_el.text.strip()
        return order_number
    
    def click_to_feed(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED)

    def find_order_in_feed(self, my_order):
        order_in_feed = self.find_element_with_wait(FeedPageLocators.FEED)
        return my_order in order_in_feed.text
    
    def open_feed_load_counters(self):
            self.open()
            self.find_element_with_wait(FeedPageLocators.FEED)
            self.find_element_with_wait(FeedPageLocators.COUNTER_TODAY_DONE)

    def my_order_in_order_in_feed(self, my_order):
        my_order_str = f"{int(my_order):07d}"
        order_in_feed = self.find_element_with_text(FeedPageLocators.IN_WORK_ORDER_NUMBERS, my_order_str)
        return (my_order in order_in_feed)

    
        


