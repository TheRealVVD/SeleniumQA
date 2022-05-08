import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(8)
    basket_button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert 'Ajouter au panier' == basket_button.text, 'Хуйня'



# pytest --language=es Lesson3\3.6\task9\test_items.py



