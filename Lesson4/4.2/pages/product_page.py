import pytest
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    name = ""
    price = ""

    def should_be(self):
        self.should_be_right_url()
        self.should_be_buy_button()

    def should_be_buy_button(self):
        self.browser.find_element(*ProductPageLocators.BUY_BUTTON).click()

    def should_be_right_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Пиздеж чистой воды"

    def find_name_price(self):
        self.name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        self.price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text.split("&")[0]

    def check(self):
        self.should_be_right_book_name()
        self.should_be_right_book_price()

    def should_be_right_book_name(self):
        assert self.name == self.browser.find_element(*ProductPageLocators.NAME_ASSERT).text, "Book's names are different"

    def should_be_right_book_price(self):
        assert self.price in self.browser.find_element(*ProductPageLocators.PRICE_ASSERT).text, "Book's prices are different"

    def random_wait(self):
        self.wait(*ProductPageLocators.RANDOM_WINDOW)

    def should_be_right_url2(self, url):
        print(self.url)
        print(self.browser.current_url)
        assert self.url == self.browser.current_url, "Пиздеж чистой воды2"


