### Задание: независимость контента, ищем баг
Эта задача для настоящих ниндзя автотестинга. Не потому что она сложная, а потому что сейчас мы будем ловить с вами настоящий баг с помощью наших автотестов. Для нашего интернет-магазина было запущено несколько новых промо-акций, одна из которых привела к появлению бага. Промо-акция включается путем добавления параметра ?promo=offerN к ссылке на товар.

К счастью, нам не придется менять наш тест, чтобы проверить изменения в коде. Мы просто запустим всё тот же тест на странице http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/ с параметризацией. Вам нужно определить, при каком значении параметра promo автотест упадет. Для этого проверьте результат работы PyTest и найдите url, на котором произошла ошибка. Значение параметра может изменяться от offer0 до offer9.

Пример ссылки: http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0. Если баг будет найден на этой странице, то введите в качестве ответа http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0.

Запустить сразу несколько тестов вы можете, используя **@pytest.mark.parametrize**. Мы уже сделали для вас шаблон теста:

```python
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # ваша реализация теста
```
Подсказка: баг должен быть найден методом проверки.

После того как вы обнаружили баг, учитывая что чинить его не собираются, лучше всего пометить падающий тест как **xfail** или **skip**. Помните, как мы такое проворачивали в третьем модуле? Освежить память: [XFail: помечать тест как ожидаемо падающий][1].

[1]: https://stepik.org/lesson/236918/step/5?unit=209305

С параметризацией делается это примерно так:  
```python
@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])
```
Подробнее: [Skip/xfail with parametrize][2]

[2]: https://pytest.org/en/stable/skipping.html#skip-xfail-with-parametrize