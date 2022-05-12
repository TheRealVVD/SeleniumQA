from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    URL = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUY_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    NAME_ASSERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    PRICE_ASSERT = (By.CSS_SELECTOR, "div.alertinner p strong")
    RANDOM_WINDOW = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div ")
