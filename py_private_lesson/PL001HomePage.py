from selenium.webdriver.support.wait import WebDriverWait
from properties import test_data

class PL001HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_homepage(self):

        self.driver.get(test_data.pv_lessons_url)
