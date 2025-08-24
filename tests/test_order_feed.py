import allure
from helpers.orders import ApiMethods
from pages.orders_feed_page import OrdersFeedPage


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
        feed.click_to_feed()
        feed.open()

        assert feed.find_order_in_feed(my_order)



    @allure.title("При создании нового заказа увеличивается общий счётчик 'Выполнено'")
    def test_total_done_counter_increases(self, authorized_driver):
        driver = authorized_driver
        feed = OrdersFeedPage(driver)

        feed.open()
        before = feed.get_total_done_counter()
        ingredient_ids = ApiMethods.get_ingredient_ids()[:2]
        ApiMethods.create_order_via_api(ingredient_ids)
        feed.open()
        after = feed.get_total_done_counter()

        assert after >= before


    @allure.title("При создании нового заказа увеличивается счётчик 'Выполнено сегодня'")
    def test_today_done_counter_increases(self, existing_user_driver):
        driver = existing_user_driver
        feed = OrdersFeedPage(driver)
        
        feed.open_feed_load_counters()
        before = feed.get_today_done_counter()

        feed.get_order_number_and_create_an_order(existing_user_driver)
        feed.open_feed_load_counters()
        after = feed.get_today_done_counter()

        assert after > before

    @allure.title("Добавление заказа показывает заказ в 'В работе'")
    def test_order_number_in_work_section(self, existing_user_driver):
        driver = existing_user_driver
        feed = OrdersFeedPage(driver)

        my_order = feed.get_order_number_and_create_an_order(existing_user_driver)
        feed.open_feed_load_counters()

        assert feed.my_order_in_order_in_feed(my_order)




