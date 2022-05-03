'''
Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. '''

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