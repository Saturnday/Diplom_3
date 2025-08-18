import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.locators import MainPageLocators, LoginPageLocators
from selenium.common.exceptions import TimeoutException
from data.data import TestData



@allure.suite("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_click_profile_button(self, authorized_driver):

        driver = authorized_driver
        main_page = MainPage(driver)

        main_page.wait_for_overlay_to_disappear()
        main_page.click_profile_button()


        assert "profile" in driver.current_url or main_page.find_element_with_wait(MainPageLocators.NAME)


    @allure.title("переход в раздел «История заказов»")
    def test_check_history(self, authorized_driver):

        driver = authorized_driver
        main_page = MainPage(driver)

        main_page.wait_for_overlay_to_disappear()
        main_page.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)
        main_page.click_order_feed_button()

        assert "order-history" in driver.current_url or main_page.find_element_with_wait(LoginPageLocators.ORDERS_READY)
        

    #!!!!logout button is not clickable within the selenium execution, the locator is correct, but the button itself is always inacive
    @allure.title("Выход из аккаунта - Не работает под селениумом")
    def test_logout(self, existing_user_driver):
        login_page = LoginPage(existing_user_driver)
        main_page = MainPage(existing_user_driver)

        login_page.open()
        login_page.click_to_element_with_wait(MainPageLocators.BUTTON_PROFILE)
        main_page.wait_for_page_ready()
        main_page.wait_for_overlay_to_disappear()
        main_page.find_element_with_wait(MainPageLocators.BUTTON_LOGOUT)
        main_page.click_to_element_with_wait(MainPageLocators.BUTTON_LOGOUT)

        restore_link = main_page.find_element_with_wait(LoginPageLocators.LINK_RESTORE_PASSWORD, timeout=10)
        assert restore_link.is_displayed()


        




