from locators.locators import LoginPageLocators, MainPageLocators
from pages.base_page import BasePage
from data.data import TestData
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage(BasePage):
    URL = TestData.url('login')

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_page_ready()

    def login(self, email, password):
        self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.find_element_with_wait(LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        self.find_element_with_wait(LoginPageLocators.BUTTON_LOGIN).click()

    def restore_password(self, email):
        self.find_element_with_wait(LoginPageLocators.LINK_RESTORE_PASSWORD).click()
        self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.find_element_with_wait(LoginPageLocators.BUTTON_RESTORE).click()

    def toggle_show_password(self, password):
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)
        self.find_element_with_wait(LoginPageLocators.INPUT_NEW_PASSWORD).send_keys(password)
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)
        self.find_element_with_wait(LoginPageLocators.SHOW_PASSWORD).click()
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)



    def is_password_field_active(self):
        self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_to_disappear(MainPageLocators.OVERLAY)
        input_element = self.find_element_with_wait(LoginPageLocators.PASSWORD)
        class_attribute = input_element.get_attribute("class")
        return "input_status_active" in class_attribute



    def login_with_credentials(self, email, password):
        email_input = self.find_element_with_wait(LoginPageLocators.INPUT_EMAIL)
        self.click_to_element_with_wait(LoginPageLocators.INPUT_EMAIL)
        email_input.send_keys(email)

        password_input = self.find_element_with_wait(LoginPageLocators.INPUT_PASSWORD)
        self.click_to_element_with_wait(LoginPageLocators.INPUT_PASSWORD)
        password_input.send_keys(password)
        self.click_login()

    def click_login(self):
            ActionChains(self.driver).move_by_offset(0, 0).click().perform()
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(*LoginPageLocators.BUTTON_LOGIN))
            )
            login_btn.click()