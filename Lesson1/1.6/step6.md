###Поиск всех необходимых элементов с помощью find_elements_by

Мы уже упоминали, что метод find_element_by возвращает только первый из всех элементов, которые подходят под условия поиска. Иногда возникает ситуация, когда у нас есть несколько одинаковых по сути объектов на странице, например, иконки товаров в корзине интернет-магазина. В тесте нам нужно проверить, что отображаются все выбранные для покупки товары. Для этого существуют методы find_elements_by, которые в отличие от find_element_by вернут список всех найденных элементов по заданному условию. Проверив длину списка, мы можем удостовериться, что в корзине отобразилось правильное количество товаров. Пример кода (код приведен только для примера, сайта fake-shop.com скорее всего не существует):
```
# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
browser.get("https://fake-shop.com/book1.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# открываем страницу второго товара
browser.get("https://fake-shop.com/book2.html")

# добавляем товар в корзину
add_button = browser.find_element_by_css_selector(".add")
add_button.click()

# тестовый сценарий
# открываем корзину
browser.get("https://fake-shop.com/basket.html")

# ищем все добавленные товары
goods = browser.find_elements_by_css_selector(".good")

# проверяем, что количество товаров равно 2
assert len(goods) == 2
```
Набор стратегий здесь такой же, как и в случае с **find_element_by**:

- find_elements_by_css_selector;
- find_elements_by_xpath;
- find_elements_by_name;
- find_elements_by_tag_name;
- find_elements_by_class_name;
- find_elements_by_link_text;
- find_elements_by_partial_link_text.

Также для поиска нескольких элементов мы можем использовать универсальный метод find_elements вместе с атрибутами класса **By**:
```
from selenium.webdriver.common.by import By

browser.find_elements(By.CSS_SELECTOR, "button.submit")
```
*!Важно*. Обратите внимание на важную разницу в результатах, которые возвращают методы **find_element** и f**ind_elements**. Если первый метод не смог найти элемент на странице, то он вызовет ошибку NoSuchElementException, которая прервёт выполнение вашего кода. Второй же метод всегда возвращает валидный результат: если ничего не было найдено, то он вернёт пустой список и ваша программа перейдет к выполнению следующего шага в коде.