from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math, os

link = 'http://suninjuly.github.io/file_input.html'

folder_path = os.path.abspath(os.path.dirname('lesson2.2_step8.py'))
file_path = os.path.join(folder_path, 'text.txt')
print(file_path)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys('Vlados')

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys('Bratos')

    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('vlados@bratos.vb')

    button_load = browser.find_element(By.ID, 'file')
    # button_load.click() # кнопку на надо нажимать
    button_load.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()

finally:
    time.sleep(15)
    browser.quit()






