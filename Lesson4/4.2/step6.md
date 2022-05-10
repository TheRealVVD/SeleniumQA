### Проверка элемента на странице
Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и перехватывать исключения.

Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам ```True``` или ```False```. Можно сделать это по-разному (с настройкой явных или неявных ожиданий). Сейчас воспользуемся неявным ожиданием.

1. В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:

```python
def __init__(self, browser, url, timeout=10):
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)
```
2. Теперь в этом же классе реализуем метод ```is_element_present```, в котором будем перехватывать исключение. В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 

Чтобы перехватывать исключение, нужна конструкция ```try/except```: 

```python
def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except (имя исключения):
        return False
    return True
```
Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 

```python
from selenium.common.exceptions import имя_исключения
```
Отлично! Теперь для всех проверок, что элемент действительно присутствует на странице, мы можем использовать этот метод. 

3. Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке: 

```python
def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
```
Запустите тесты и посмотрите, что вывод об ошибке стал более понятным: 

```pytest -v --tb=line --language=en test_main_page.py```