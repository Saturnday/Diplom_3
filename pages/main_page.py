import allure
from data.data import TestData
from pages.base_page import BasePage
from locators.locators import MainPageLocators



class MainPage(BasePage):

    URL = 'https://stellarburgers.nomoreparties.site/'

    @allure.step("Открыть главную страницу")
    def open(self, url=None):
        self.open_url(url or self.URL)

    @allure.step("Клик на конструктор заказов")
    def click_constructor_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.click_to_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Клик на Заказы")
    def click_order_feed_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED).click()
        self.wait_for_page_ready()
        self.wait_for_overlays_to_disappear([MainPageLocators.MODAL_OVERLAY, MainPageLocators.OVERLAY], timeout=15)

    @allure.step("Получить колличество заказов")
    def get_order_counter(self, name):
        locator = MainPageLocators.counter_by_ingredient_name(name)
        element = self.find_element_with_wait(locator)
        return element.text
    
    @allure.step("Клик на кнопку профиля")
    def click_profile_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PROFILE).click()

    @allure.step("Ожидание исчезновения оверлея")
    def wait_for_overlay_to_disappear(self):
        try:
            self.wait_for_element_to_disappear(MainPageLocators.OVERLAY)
        except:
            pass

    def wait_for_overlay_2_to_disappear(self):
        try:
            self.wait_for_element_to_disappear(MainPageLocators.MODAL_OVERLAY)
        except:
            pass
    
    @allure.step("Клик на кнопку выхода из аккаунта")
    def click_logout(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_LOGOUT)
    
    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_to_element_with_wait(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Ожидание загрузки списка ингредиентов")
    def wait_for_ingredients_loaded(self, ingredient_locator, overlay_locators, timeout=15):
        self.wait_for_page_ready(timeout=timeout)
        self.wait_for_overlays_to_disappear(overlay_locators, timeout=5)
        elements = self.find_elements_with_wait(ingredient_locator, timeout=timeout)
        if elements:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elements[0])
        return elements

    @allure.step("Открыть модальное окно ингредиента")
    def open_ingredient_modal(self, ingredient_name):
        ingredient_locator = MainPageLocators.get_ingredient_locator(ingredient_name)

        self.click_to_element_with_wait(ingredient_locator)
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Закрыть окно с ингридиентом")
    def close_ingredient_modal(self):
        self.click_to_element_with_wait(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)
    
    @allure.step("Клик на кнопку профиля")
    def click_profile_button(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_PROFILE, timeout=15)


    @allure.step("Проверить, открыта ли страница профиля")
    def is_profile_page_opened(self, timeout=10):
        self.wait_for_page_ready(timeout)
        try:
            return "profile" in self.get_current_url or self.find_element_with_wait(MainPageLocators.NAME, timeout=timeout)
        except Exception:
            return False

    @allure.step("Проверить, открыта ли страница истории заказов")
    def is_order_history_page_opened(self, timeout=10):
        self.wait_for_page_ready(timeout)
        try:
            return "order-history" in self.get_current_url or self.find_element_with_wait(MainPageLocators.ORDERS_READY, timeout=timeout)
        except Exception:
            return False
    
    @allure.step("Найти элемент: игридиент")
    def ingredient_found(self):
        try:
            self.find_element_with_wait(MainPageLocators.INGREDIENT_ITEM)
            return True
        except:
            False

    @allure.step("Найти элемент: счетчик заказов")
    def find_element_in_order_feed(self, feed_locator):
        try:
            self.wait_for_page_ready()
            self.find_element_with_wait(feed_locator)
            return True
        except:
            return False

    @allure.step("Найти элемент: булки детали")
    def find_bun_details(self):
        try:
            self.find_element_with_wait(MainPageLocators.BUN_DETAILS)
            return True
        except Exception:
            return False
        
    @allure.step("Заказ в работе")
    def order_in_process(self):
        try:
            self.find_element_with_wait(MainPageLocators.ORDER_IN_PROCESS)
            return True
        except Exception:
            return False
        
    @allure.step('Проверить отображение линки восстановление пароля')
    def restore_link_is_displayed(self):
        restore_link = self.find_element_with_wait(MainPageLocators.LINK_RESTORE_PASSWORD, timeout=10)
        try:
            restore_link.is_displayed()
            return True
        except:
            return False

    @allure.step('Создать заказ')
    def create_an_order(self):
        self.click_to_element_with_wait(MainPageLocators.LOGIN)
        self.add_ingredient_to_constructor(TestData.CONSTRUCTOR[1])
        self.click_to_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)

    @allure.step("Ожидание изменения счетчика ингредиента")
    def wait_for_counter_change(self, ingredient_name, initial_value, timeout=6):
        return self.wait_for_condition(
            lambda d: self.get_order_counter(ingredient_name) != initial_value,
            timeout
        )
