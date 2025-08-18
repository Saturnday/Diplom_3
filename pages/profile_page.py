from locators.locators import ProfilePageLocators
from pages.base_page import BasePage

class ProfilePage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/account/profile"

    def open(self):
        self.driver.get(self.URL)

    def click_profile_button(self):
        self.find_element_with_wait(ProfilePageLocators.BUTTON_PROFILE).click()

    def click_order_history(self):
        self.find_element_with_wait(ProfilePageLocators.BUTTON_ORDER_HISTORY).click()

    def click_logout(self):
        self.find_element_with_wait(ProfilePageLocators.BUTTON_LOGOUT).click()

    def is_logout_button_displayed(self):
        return self.find_element_with_wait(ProfilePageLocators.BUTTON_LOGOUT).is_displayed()

    