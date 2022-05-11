'''
Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
    wait = WebDriverWait(browser, 12)
    price_field = wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button2 = browser.find_element(By.ID, 'book')
    button2.click()

    x_element = browser.find_element(By.ID, 'input_value')
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element) # скроллим до значения Х
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    submit = browser.find_element(By.ID, 'solve')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
