from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPageLocators:
    INPUT_EMAIL = (By.NAME, "name")
    INPUT_PASSWORD = (By.NAME, 'Пароль')
    BUTTON_LOGIN = (By.XPATH, "//button[contains(text(),'Войти')]")
    LINK_RESTORE_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')
    BUTTON_RESTORE = (By.XPATH, '//button[text()="Восстановить"]')
    TEXT_RESTORE = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    SHOW_PASSWORD = (By.CSS_SELECTOR, "div[class='input__icon input__icon-action'] svg")
    INPUT_NEW_PASSWORD = (By.XPATH, '//input[@name="Введите новый пароль"]')
    PASSWORD = (By.XPATH, '//label[contains(text(), "Пароль")]/parent::div')
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")

class MainPageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')
    BUTTON_ORDER_FEED = (By.XPATH, '//p[contains(text(),"Лента Заказов")]')
    INGREDIENT_ITEM = (By.XPATH, '//p[text()="Соус фирменный Space Sauce"]')  
    ORDER_COUNTER = (By.XPATH, '//span[@class="counter_counter__num__3nV4z"]')
    READY_ORDERS_COUNTER = (By.XPATH, '//p[contains(text(),"Выполнено за все время")]')
    BUTTON_PROFILE = (By.XPATH, '//p[text()="Личный Кабинет"]')
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
    NAME = (By.XPATH, "//label[contains(text(),'Имя')]")
    BUTTON_PROFILE = (By.XPATH, '//p[text()="Личный Кабинет"]')
    BUTTON_ORDER_HISTORY = (By.XPATH, '//a[text()="История заказов"]')
    BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(),'Выход')]")
    ORDERS_READY = (By.XPATH, "//p[contains(text(),'Готовы:')]")
    LINK_RESTORE_PASSWORD = (By.XPATH, '//a[text()="Восстановить пароль"]')

    BUNS = (By.XPATH, "//span[text()='Булки']")
    # Соусы
    SAUCES = (By.XPATH, "//span[text()='Соусы']")
    # Начинки
    FILLINGS = (By.XPATH, "//span[text()='Начинки']")

    INGREDIENTS = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient_1TVf6")
    INGREDIENT_MODAL = (By.CSS_SELECTOR, "div.Modal_modal_opened__3ISw4")
    BUTTON_CLOSE_MODAL = (By.CSS_SELECTOR, "button.Modal_modal__close")
    INGREDIENT_LINKS = (By.CSS_SELECTOR, "a.BurgerIngredient_ingredient_1TVf6")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//div[contains(@class,'Modal') or contains(@class,'modal')]//h2")
    INGREDIENT_MODAL_CLOSE = (By.TAG_NAME, "button")
    
    BUN_1 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    BUN_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")

    ELEMENT_TO = (By.XPATH, "//span[contains(text(), 'Перетяните булочку сюда')]")

    @staticmethod
    def ingredient_by_name(name):
        return By.XPATH, f"//p[contains(text(), '{name}')]"
    
    @staticmethod
    def counter_by_ingredient_name(name):
        return By.XPATH, (
            f"//p[contains(text(), '{name}')]/ancestor::a"
            f"//p[contains(@class, 'counter_counter__num')]"
        )

    BUTTON_MAKE_ORDER = (By.XPATH, "//button[contains(text(), 'Оформить')]")
    ORDER_IN_PROCESS = (By.XPATH, "//p[contains(text(), 'готовить')]")
    LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ORDER_NUMBER = (By.XPATH, "//p[text()='идентификатор заказа']/preceding-sibling::h2")
    CLOSER_ORDER = (By.CLASS_NAME, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")
    CLOSE_ORDER_WINDOW_BUTTON = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button")


class ProfilePageLocators:
    BUTTON_PROFILE = (By.XPATH, "//a[@href='/account/profile']")
    BUTTON_ORDER_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")
    
class FeedPageLocators:
    FEED_ORDER_ITEM = (By.CLASS_NAME, 'OrderHistory_link__1iNby')
    FEED_ORDER_MODAL = (By.XPATH, '//p[contains(text(), "Cостав")]')
    ALL_ORDER_NUMBERS = (By.CSS_SELECTOR, 'a.order-card span.number, div.order-card span.number')
    COUNTER_TOTAL_DONE = (By.CSS_SELECTOR, 'p.total-done, #total-done')
    COUNTER_TODAY_DONE = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')
    FEED = (By.CLASS_NAME, 'OrderFeed_orderList__cBvyi')
    IN_WORK_ORDER_NUMBERS = (By.XPATH, "//p[contains(text(), 'В работе')]/following-sibling::ul[2]/li")