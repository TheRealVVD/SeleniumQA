import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class TestLogin:
    @pytest.mark.parametrize('num', [i for i in range(236895, 236900)])
    def test_guest_should_see_login_link(self, browser, num):
        link = f"https://stepik.org/lesson/{num}/step/1"
        browser.implicitly_wait(7)
        browser.get(link)
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        wait = WebDriverWait(browser, 5)
        textarea = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        )
        assert "Correct!" == textarea.text, 'Wrong textarea suka'


    @pytest.mark.parametrize('nums', [i for i in range(236903, 236906)])
    def test_guest_should_see_navbar_element(self, browser, nums):
        link = f"https://stepik.org/lesson/{nums}/step/1"
        browser.implicitly_wait(7)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "textarea[spellcheck='false']").send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        wait = WebDriverWait(browser, 5)
        textarea = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))
        )
        assert "Correct!" == textarea.text, 'Wrong textarea suka'

        #pytest -s -v Lesson3\3.6\lesson6_step3.py