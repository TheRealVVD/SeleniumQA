import time
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

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
            # time.sleep(500)
        except NoAlertPresentException:
            print("No second alert presented")

    def wait(self, how, what):
        wait = WebDriverWait(self.browser, 7)
        score = wait.until(
            EC.presence_of_element_located((how, what))
        )
