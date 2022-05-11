from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


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
    page.should_be_buy_button()
    page.solve_quiz_and_get_code()

# pytest -v --tb=line Lesson4\4.2\test_main_page.py
# pytest -v --tb=line Lesson4\4.2\test_main_page.py::test_url
# pytest -v -s --tb=line Lesson4\4.2\test_main_page.py::test_guest_can_add_product_to_basket

