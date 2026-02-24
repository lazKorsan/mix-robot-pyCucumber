# practice_software_pages.py
# C:\Users\user\PycharmProjects\exantring\pages\practice_software_pages.py

import time
from selenium.webdriver.support.ui import WebDriverWait
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

practice_software_loginButton_Xpath='//*[@data-test="nav-sign-in"]'
practice_software_emailBox_Xpath='//input[@id="email"]'
practice_software_passwordBox_Xpath='//input[@id="password"]'
practice_software_loginButton_Xpath2='//input[@data-test="login-submit"]'
practice_software_homePage="https://practicesoftwaretesting.com/"
practice_software_email="lazKorsan@gmail.com"
practice_software_password = "Query.2026"


class PracticeSoftwarePage:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, driver=None):
        self._driver = driver
        self._wait = None
        if driver:
            self._wait = WebDriverWait(self._driver, 10)

    @property
    def driver(self):
        if self._driver is None:
            try:
                self._driver = BuiltIn().get_library_instance('SeleniumLibrary').driver
                self._wait = WebDriverWait(self._driver, 10)
            except Exception as e:
                print(f"Driver bulunamadı: {e}")
        return self._driver

    @keyword("Navigate To Practice Software Home Page")
    def navigate_practice_software_homePage(self, url=practice_software_homePage):
        self.driver.get(url)

    @keyword("Navigate To Practice Software Login Page")
    def navigate_to_practice_software_loginPage(self):
        click_utils(
            self.driver,
            practice_software_loginButton_Xpath
        )
        time.sleep(2)

    @keyword("Practice Software Login")
    def practice_software_login(self, mail=practice_software_email, password=practice_software_password):
        # login islemlerini gerçekleştirir.
        sendKey_utils(
            self.driver,
            practice_software_emailBox_Xpath,
            mail
        )

        # şifreyi girer
        sendKey_utils(
            self.driver,
            practice_software_passwordBox_Xpath,
            password
        )

        # login butonuna tıklar
        click_utils(
            self.driver,
            practice_software_loginButton_Xpath2
        )
