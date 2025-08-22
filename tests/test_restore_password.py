import allure
from pages.login_page import LoginPage

@allure.suite("Восстановить пароль")
class TestRestorePassword:
    
    @allure.step("Переход на страницу восстановления пароля по кнопке ‘Восстановить пароль’")
    def test_navigate_to_restore_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_link_resotre_password()
        
        assert login_page.is_restore_password_page_opened()

    @allure.step("Ввод почты и клик по кнопке ‘Восстановить’")
    def test_restore_password_with_email(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.restore_password()

        assert login_page.is_reset_password_page_opened()
    
    @allure.step("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_hide_password_field_focus(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.restore_password_show_password()
        
        assert login_page.is_password_field_active()