from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be(self):
        self.should_be_right_url()
        self.should_be_buy_button()

    def should_be_buy_button(self):
        self.browser.find_element(*ProductPageLocators.BUY_BUTTON).click()

    def should_be_right_url(self):
        assert "promo=newYear" in self.browser.current_url, "Пиздеж чистой воды"
