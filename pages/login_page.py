import allure
from data.data import TestData
from pages.base_page import BasePage
from locators.locators import LoginPageLocators

class LoginPage(BasePage):
    URL = TestData.url('login')

    @allure.step("Открытие страницы логина")
    def open(self):
        self.open_url(self.URL)
        self.wait_for_page_ready()

    @allure.step("Вход в систему с email и паролем")
    def login(self, email, password):
        self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.find_element_with_wait(LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.find_element_with_wait(LoginPageLocators.BUTTON_LOGIN).click()

    @allure.step("Проверяет, что мы на странице восстановления пароля")
    def is_restore_password_page_opened(self):
        return "forgot-password" in self.get_current_url()

    @allure.step("Восстановление пароля по email")
    def restore_password(self, email):
        email = TestData.EXISTING_EMAIL
        self.find_element_with_wait(LoginPageLocators.LINK_RESTORE_PASSWORD).click()
        self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.find_element_with_wait(LoginPageLocators.BUTTON_RESTORE).click()
        
    @allure.step("Проверем открыта ли страица сброса пароля")
    def is_reset_password_page_opened(self):
        return "reset-password" in self.get_current_url()

    @allure.step("Переключение видимости поля пароля")
    def toggle_show_password(self, password):
        self.wait_for_element_to_disappear(LoginPageLocators.MODAL_OVERLAY)
        self.find_element_with_wait(LoginPageLocators.INPUT_NEW_PASSWORD).send_keys(password)
        self.wait_for_element_to_disappear(LoginPageLocators.MODAL_OVERLAY)
        self.find_element_with_wait(LoginPageLocators.SHOW_PASSWORD).click()
        self.wait_for_element_to_disappear(LoginPageLocators.MODAL_OVERLAY)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        self.wait_for_element_to_disappear(LoginPageLocators.MODAL_OVERLAY)
        self.wait_for_element_to_disappear(LoginPageLocators.OVERLAY)
        input_element = self.find_element_with_wait(LoginPageLocators.PASSWORD)
        class_attribute = input_element.get_attribute("class")
        return "input_status_active" in class_attribute
    
    @allure.step("Вход в систему с использованием учетных данных")
    def login_with_credentials(self, email, password):
        email_input = self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL)
        self.click_to_element_with_wait(LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)

        password_input = self.find_element_with_wait(LoginPageLocators.INPUT_PASSWORD)
        self.click_to_element_with_wait(LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys(password)
        self.click_login()

    @allure.step("Клик на: логин")
    def click_login(self):
        self.find_element_with_wait(LoginPageLocators.BUTTON_LOGIN)
        self.click_to_element_with_wait(LoginPageLocators.BUTTON_LOGIN)
    
    @allure.step("Клик на: тугл показать пароль")
    def restore_password_show_password(self):
        self.restore_password(TestData.EXISTING_EMAIL)
        self.toggle_show_password(TestData.EXISTING_PASSWORD)

    @allure.step("Клик на: посстановить пароль")
    def click_link_resotre_password(self):
        self.click_to_element_with_wait(LoginPageLocators.LINK_RESTORE_PASSWORD)