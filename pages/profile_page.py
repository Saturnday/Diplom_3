from locators.locators import ProfilePageLocators
from pages.base_page import BasePage
import allure

class ProfilePage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site/account/profile"

    @allure.step("Открыть страницу профиля")
    def open(self):
        self.open_url(self.URL)

    @allure.step("Нажать на кнопку 'Профиль'")
    def click_profile_button(self):
        self.find_element_with_wait(ProfilePageLocators.BUTTON_PROFILE).click()

    @allure.step("Нажать на кнопку 'История заказов'")
    def click_order_history(self):
        self.find_element_with_wait(ProfilePageLocators.BUTTON_ORDER_HISTORY).click()

    @allure.step("Нажать на кнопку 'Выход'")
    def click_logout(self):
        self.find_element_with_wait(ProfilePageLocators.BUTTON_LOGOUT).click()

    @allure.step("Проверить отображение кнопки 'Выход'")
    def is_logout_button_displayed(self):
        return self.find_element_with_wait(ProfilePageLocators.BUTTON_LOGOUT).is_displayed()

    