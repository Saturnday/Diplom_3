import allure
from pages.main_page import MainPage


@allure.suite("Личный кабинет")
class TestProfile:

    @allure.step("Переход по клику на «Личный кабинет»")
    def test_click_profile_button(self, authorized_driver):

        driver = authorized_driver
        main_page = MainPage(driver)

        main_page.wait_for_overlay_to_disappear()
        main_page.click_profile_button()
        
        assert main_page.is_profile_page_opened()


    @allure.step("переход в раздел «История заказов»")
    def test_check_history(self, authorized_driver):

        driver = authorized_driver
        main_page = MainPage(driver)

        main_page.wait_for_overlay_to_disappear()
        main_page.wait_for_overlay_2_to_disappear()
        main_page.click_order_feed_button()

        assert main_page.is_order_history_page_opened()
        

    #!!!!logout button is not clickable within the selenium execution, the locator is correct, but the button itself is always inacive
    @allure.step("Выход из аккаунта - Не работает под селениумом")
    def test_logout(self, existing_user_driver):

        driver = existing_user_driver
        main_page = MainPage(driver)

        main_page.open()
        main_page.click_profile_button()
        main_page.wait_for_page_ready()
        main_page.wait_for_overlay_to_disappear()
        main_page.click_logout()

        assert main_page.restore_link_is_displayed()



        




