'''
Задание: поиск элементов с помощью Selenium
Вам нужно открыть страницу по ссылке и заполнить форму на этой странице с помощью Selenium. Если всё сделано правильно, то вы увидите окно с проверочным кодом. Это число вам нужно ввести в качестве ответа в этой задаче.

!Обратите внимание, что время для ввода данных ограничено. Однако благодаря Selenium вы сможете выполнить задачу до того, как время истечёт.
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

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
    time.sleep(15) # время, чтобы скопировать код
    browser.quit()

# не забываем оставить пустую строку в конце файла