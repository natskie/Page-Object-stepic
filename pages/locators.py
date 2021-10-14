from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON=(By.CSS_SELECTOR, ".basket-mini .btn-default")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON_ADD=(By.CSS_SELECTOR, "button.btn-add-to-basket")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    BASKET_STRONG_NAMES = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, ".alert-success")  

class BasketPageLocators():
    ITEMS = (By.CSS_SELECTOR, "#content_inner #basket_formset")
    EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")