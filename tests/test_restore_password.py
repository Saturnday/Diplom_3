import allure
from pages.login_page import LoginPage
from data.data import TestData
from locators.locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Restore Password")
class TestRestorePassword:
    
    @allure.title("Переход на страницу восстановления пароля по кнопке ‘Восстановить пароль’")
    def test_navigate_to_restore_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.find_element_with_wait(LoginPageLocators.LINK_RESTORE_PASSWORD).click()
        assert "forgot-password" in driver.current_url

    @allure.title("Ввод почты и клик по кнопке ‘Восстановить’")
    def test_restore_password_with_email(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.restore_password(TestData.EXISTING_EMAIL)
        assert "reset-password" in driver.current_url or login_page.find_element_with_wait(LoginPageLocators.TEXT_RESTORE)
    
    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_hide_password_field_focus(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.restore_password(TestData.EXISTING_EMAIL)
        login_page.toggle_show_password(TestData.EXISTING_PASSWORD)
        assert login_page.is_password_field_active()