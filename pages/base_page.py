from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from data.data import TestData
from helpers.orders import GetLocators

import allure

class BasePage:

    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step('Открыть линку')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Клик на элемент')
    def click_to_element_with_wait(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).move_by_offset(0, 0).click().perform()

    @allure.step('Найти элемент')
    def find_element_with_wait(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ждать загрузки страницы')
    def wait_for_page_ready(self, timeout=15):

        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
    @allure.step('Ждать пока элемент не исчезнет')
    def wait_until_element_is_visible(self, locator, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return None
        
    @allure.step('Ждать пока элемент исчезнет')
    def wait_until_element_is_not_visible(self, locator, timeout=5):

        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            pass

    @allure.step('Закрыть попап ESC и ждать исчезновения элемента')
    def wait_for_element_to_disappear(self, locator, timeout = 15):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((locator)))
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((locator)))

    @allure.step('Close popup with ESC')
    def esc(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    @allure.step('Drag and Drop an element (Chrome)')
    def drag_and_drop_element_chrome(self, element_from, element_to):
        from_element = self.find_element_with_wait(element_from)
        to_element = self.find_element_with_wait(element_to)
        ActionChains(self.driver).drag_and_drop(from_element, to_element).perform()

    @allure.step('Drag and Drop an element (Firefox workaround)')
    def drag_and_drop_element_firefox(self, locator_from, locator_to):
        from_element = self.find_element_with_wait(locator_from)
        to_element = self.find_element_with_wait(locator_to)
        self.driver.execute_script("""
        const [from_element, to_element] = arguments;
        const dataTransfer = new DataTransfer();
        ['dragstart', 'dragover', 'drop', 'dragend'].forEach(eventType => {
            const event = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
            (eventType === 'dragstart' ? from_element : to_element).dispatchEvent(event);
        });
        """, from_element, to_element)

    def find_elements_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_elements(*locator)
        )
    
    @allure.step('Ждать пока текст элемента изменится (не будет заданного)')
    def wait_until_element_text_is_not(self, locator, text, timeout=15):
        WebDriverWait(self.driver, timeout).until_not(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Ждать пока текст элемента изменится (не будет unwanted_text)')
    def wait_until_text_is_not(self, locator, unwanted_text, timeout=20):

        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() != unwanted_text
        )
        return self.driver.find_element(*locator).text.strip()
    
    @allure.step('Ждать пока текст элемента поменяется')
    def wait_until_text_changes(self, locator, old_text, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text.strip() != old_text
        )
        return self.driver.find_element(*locator).text.strip()

    @allure.step('Ждать пока заглушка не исчезнет')
    def wait_until_order_number_is_real(self, locator, placeholder='9999', timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda d: (el := self.find_element_with_wait(locator)).text.strip() != placeholder
        )
        
        order_number = self.find_element_with_wait(locator).text.strip()
        return order_number
    
    @allure.step('Скрол к элементу')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Найти элемент с заданным текстом')
    def find_element_with_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
        order_in_feed = self.find_element_with_wait(locator).text
        return order_in_feed
    
    @allure.step("Ожидание выполнения условия")
    def wait_for_condition(self, condition, timeout=6):
        return WebDriverWait(self.driver, timeout).until(condition)
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Получить имя браузера")
    def get_browser_name(self):
        return self.driver.capabilities["browserName"].lower()
    
    @allure.step("Создать заказ и получить его номер")
    def get_order_number_and_create_an_order(self, ingredient_name, login_locator, make_order_locator, order_number_locator):
        self.open_url(TestData.BASE_URL)
        self.click_to_element_with_wait(login_locator)
        self.add_ingredient_to_constructor(ingredient_name)
        self.click_to_element_with_wait(make_order_locator)  
        self.wait_until_order_number_is_real(order_number_locator, '9999') 
        order_number_el = self.find_element_with_wait(order_number_locator)
        order_number = order_number_el.text.strip()
        return order_number



    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_name):
        
        element_from = GetLocators.ingredient_by_name(ingredient_name)
        element_to = GetLocators.element_to()
        browser = self.get_browser_name()

        if browser == "chrome":
            self.drag_and_drop_element_chrome(element_from, element_to)
        elif browser == "firefox":
            self.drag_and_drop_element_firefox(element_from, element_to)
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    

    @allure.step('Ждать пока все оверлеи исчезнут')
    def wait_for_overlays_to_disappear(self, locators, timeout=10):
        for locator in locators:
            try:
                WebDriverWait(self.driver, timeout).until(
                    lambda d: not d.find_elements(*locator) or not d.find_element(*locator).is_displayed()
                )
            except TimeoutException:
                pass





