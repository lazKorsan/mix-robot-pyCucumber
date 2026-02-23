from selenium import webdriver
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

girisyapButton_Xpath='//*[@class="btn btn-success fw-bold shadow-sm px-4"]'
usernameBox_Xpath='(//input[@class="form-control border-start-0 rounded-end-3"])[1]'
passwordBox_Xpath='(//input[@class="form-control border-start-0 rounded-end-3"])[2]'
submitButton_Xpath='//button[@class="btn btn-login w-100"]'


class PrivateLessonsPage:
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def navigate_to_homepage(self,url):
        self.driver.get(url)

    def loginMethod(self, driver, userName, password):
        click_utils(self.driver,girisyapButton_Xpath)

        # userNmae box kutusuna geçerli kullanıcı adı girer
        sendKey_utils(
            driver,
            usernameBox_Xpath,
            userName
        )

        # password box kutusuna geçerli şifre girer
        sendKey_utils(
            driver,
            passwordBox_Xpath,
            password
        )

        # login butonuna tıklar
        click_utils(
            driver,
            submitButton_Xpath
        )
