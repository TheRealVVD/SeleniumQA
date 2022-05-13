from .locators import BasketPageLocators
from .base_page import BasePage
import pytest
from selenium.webdriver.common.by import By

class BasketPage(BasePage):

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS), "Items are in"

    def should_be_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Text is not in"