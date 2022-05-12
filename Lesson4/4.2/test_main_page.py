from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
import time

# def go_to_login_page(browser):
#     login_link = browser.find_element_by_css_selector("#login_link")
#     login_link.click()
#
# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     go_to_login_page(browser)

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()      # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)          # выполняем метод страницы — переходим на страницу логина
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.find_name_price()
    page.should_be()
    page.solve_quiz_and_get_code()
    page.random_wait()
    page.check()



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket2(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_right_url2(link)
    page.solve_quiz_and_get_code()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket3(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.find_name_price()
    page.should_be_right_url2(link)
    page.should_be_buy_button()
    page.solve_quiz_and_get_code()
    page.random_wait()
    page.check()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket4(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.find_name_price()
    page.should_be_right_url2(link)
    page.should_be_buy_button()
    page.solve_quiz_and_get_code()
    page.random_wait()
    page.check()

# pytest -v --tb=line Lesson4\4.2\test_main_page.py
# pytest -v --tb=line Lesson4\4.2\test_main_page.py::test_url
# pytest -v -s --tb=line Lesson4\4.2\test_main_page.py::test_guest_can_add_product_to_basket
# pytest -v -s --tb=line Lesson4\4.2\test_main_page.py::test_guest_can_add_product_to_basket2
# pytest -v -s --tb=line Lesson4\4.2\test_main_page.py::test_guest_can_add_product_to_basket3
# pytest -v -s --tb=line Lesson4\4.2\test_main_page.py::test_guest_can_add_product_to_basket4
