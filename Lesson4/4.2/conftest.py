import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    # parser.addoption('--language', action='store', default=None,
    #                  help="Choose language: es or ru"),
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")



# @pytest.fixture(scope="function")
# def browser(request):
#     print("\nstart browser for test..")
#     language = request.config.getoption("language")
#     options = Options()
#     if language == 'es':
#         options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
#         browser = webdriver.Chrome(options=options)
#     elif language == 'ru':
#         options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
#         browser = webdriver.Chrome(options=options)
#     elif language != 'es' or language != 'ru':
#         options.add_experimental_option('prefs', {'intl.accept_languages': language})
#         browser = webdriver.Chrome(options=options)
#     else:
#         raise pytest.UsageError("--language should be ru or es")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

@pytest.fixture(scope="function")
def browser(request):
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

# pytest -s -v Lesson3\3.6\task9\test_items.py
# pytest -s -v --browser_name=chrome Lesson3\3.6\task9\test_items.py
# pytest -s -v --language=nl Lesson3\3.6\task9\test_items.py
# pytest -s -v --browser_name=chrome --language=nl Lesson3\3.6\task9\test_items.py

# pytest -s -v --browser_name=firefox Lesson3\3.6\task9\test_items.py

# pytest -s -v --browser_name=chrome --language=nl Lesson3\3.6\task9\test_items.py
# pytest -v --tb=line --browser_name=chrome Lesson3\3.6\task9\test_items.py
# pytest -v --tb=line --browser_name=chrome Lesson3\3.6\task9\test_items.py