'''
Задание: вывод PyTest
Попробуйте запустить ваши тесты из урока 3.2 https://stepik.org/lesson/36285/step/13 с помощью PyTest. В выводе найдите последнюю строку, скопируйте её и отправьте в это задание. Отправьте текст, который находится между  === и ===.

PS Обратите внимание - предупреждений (warnings) в вашем ответе быть не должно.
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestURL(unittest.TestCase):
    def test_url1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
        input1.send_keys("Vlados")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
        input2.send_keys("Kentos")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
        input3.send_keys("Berk@mail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.form-control.first')
        input4.send_keys("8-800-555-3535")
        input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.form-control.second')
        input5.send_keys("Yakutia zhi est")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be a right text after the registration")

        time.sleep(1)
        browser.quit()

    def test_url2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.first')
        input1.send_keys("Vlados")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.second')
        input2.send_keys("Kentos")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.form-control.third')
        input3.send_keys("Berk@mail.com")
        input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.form-control.first')
        input4.send_keys("8-800-555-3535")
        input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block input.form-control.second')
        input5.send_keys("Yakutia zhi est")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be a right text")

        time.sleep(1)
        browser.quit()


if __name__ == "__main__":
    unittest.main()