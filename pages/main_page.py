from pages.base_page import BasePage
from locators.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    URL = 'https://stellarburgers.nomoreparties.site/'

    def open(self, url=None):
        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.URL)

    def click_constructor_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)
        self.click_to_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)

    def click_order_feed_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED).click()


    def get_order_counter(self, name):
        locator = MainPageLocators.counter_by_ingredient_name(name)
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text


    
    def click_profile_button(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PROFILE).click()

    def wait_for_overlay_to_disappear(self):
        self.wait_for_element_to_disappear(MainPageLocators.OVERLAY)
    
    def click_logout(self):
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.driver.find_element(*MainPageLocators.BUTTON_LOGOUT))
        )
        logout_btn.click()
    
    def close_ingredient_modal(self):
        self.click_to_element_with_wait(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)
    
    
    def wait_for_ingredients_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(MainPageLocators.INGREDIENT_LINKS)
        )

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            
    def open_ingredient_modal(self, ingredient_name):
        ingredient_locator = (By.XPATH, f"//span[text()='{ingredient_name}']")
        WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(ingredient_locator)
        ).click()
        return WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT_MODAL)
        )

    def close_ingredient_modal(self):
        self.click_to_element_with_wait(MainPageLocators.INGREDIENT_MODAL_CLOSE)
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL)

    def add_ingredient_to_constructor(self, ingredient_name):
        
        element_from = MainPageLocators.ingredient_by_name(ingredient_name)
        browser = self.driver.capabilities["browserName"].lower()

        if browser == "chrome":
            self.drag_and_drop_element_chrome(element_from, MainPageLocators.ELEMENT_TO)
        elif browser == "firefox":
            self.drag_and_drop_element_firefox(element_from, MainPageLocators.ELEMENT_TO)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        
    def click_profile_button(self):
        self.click_to_element_with_wait(MainPageLocators.BUTTON_PROFILE, timeout=15)
        
