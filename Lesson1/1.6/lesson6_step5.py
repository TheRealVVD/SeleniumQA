from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/find_link_text'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link_go = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link_go.click()
    time.sleep(1)
    
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Vlados")

    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Kentos")

    input3 = browser.find_element(By.CSS_SELECTOR, 'input.form-control.city')
    input3.send_keys("Berk")

    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys("Yakutia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
