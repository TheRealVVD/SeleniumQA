from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x1, x2):
        return str(int(x1) + int(x2))

    x1_element = browser.find_element(By.ID, 'num1')
    x2_element = browser.find_element(By.ID, 'num2')
    x1 = x1_element.text
    x2 = x2_element.text
    print(x1, x2)
    y = calc(x1, x2)
    print(y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()
finally:
    time.sleep(15)
    browser.quit()