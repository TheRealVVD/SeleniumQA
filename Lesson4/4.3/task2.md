### Задание: добавление в корзину со страницы товара
Давайте, прежде чем двигаться дальше, закрепим знания на практике. 

Представьте, что вы работаете тестировщиком-автоматизатором в IT-отделе интернет-магазина. QA Lead поручил вам задание автоматизировать следующий тестовый сценарий: 

1. Открываем страницу товара (http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear). Обратите внимание, что в ссылке есть параметр "?promo=newYear". Не теряйте его в авто-тесте, чтобы получить проверочный код.
2. Нажимаем на кнопку "Добавить в корзину".
3. *Посчитать результат математического выражения и ввести ответ. Используйте для этого метод **solve_quiz_and_get_code()**, который приведен ниже. Например, можете добавить его в класс **BasePage**, чтобы использовать его на любой странице. Этот метод нужен только для проверки того, что вы написали тест на Selenium. После этого вы получите код, который нужно ввести в качестве ответа на данное задание. Код будет выведен в консоли интерпретатора, в котором вы запускаете тест. Не забудьте в конце теста добавить проверки на ожидаемый результат.

Ожидаемый результат: 

1. Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
2. Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 

Тест нужно написать, используя паттерн Page Object. Для этого вам нужно: 

1. Добавить новый файл для тест-кейсов, связанных со страницей товара. Назовите файл с тестами *test_product_page.py*.
2. Создать класс Page Object для страницы товара. Опишите его в файле *product_page.py* в папке pages.
3. Описать в нем метод для добавления в корзину.
4. Дописать методы-проверки.
5. Описать необходимые локаторы к элементам страницы.
6. Написать сам тест-кейс, используя все вышеописанное. Назовите тест **test_guest_can_add_product_to_basket**.

Можете начинать работу с любого пункта, но **хорошей практикой считается написать сначала шаги и структуру теста, а потом описывать конкретную реализацию**. 

*Используйте этот метод в тесте для получения проверочного кода: 

```python
from selenium.common.exceptions import NoAlertPresentException # в начале файла

def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")
```
Чтобы увидеть проверочный код в консоли, запускайте PyTest с параметром -s:

```pytest -s test_foo.py```

