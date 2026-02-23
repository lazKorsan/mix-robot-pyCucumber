# loyal_friend_pages.py
# C:\Users\user\PycharmProjects\exantring\pages\loyal_friend_pages.py
# C:\Users\user\PycharmProjects\exantring\properties\test_data.py
# C:\Users\user\PycharmProjects\exantring\utils\click_utils.py
# C:\Users\user\PycharmProjects\exantring\utils\sendkey_utils.py



from selenium import webdriver

from properties import test_data
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils

signinButton_Xpath='(//*[@class="btn_add"])[1]'
emailBox_Xpath='(//input[@id="email"])[1]'
passwordBox_Xpath='(//input[@id="password"])[1]'
loginButton_Xpath='//button[@class="btn btn-primary btn-cons m-t-10"]'

class LoyalFriendCarePage:

    # Driver nesnesi olusturmaklıklık
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def navigate_to_home_page(self, url):
        self.driver.get(url)

    def login_method_with_valid_data(self, driver, mail, password):

        # login butonuna tıklar
        click_utils(
            self.driver,
            signinButton_Xpath
        )

        # email box kutusuna geçerli kullanıcı adı girer
        sendKey_utils(
            self.driver,
            emailBox_Xpath,
            test_data.ly_mail
        )

        # password box kutusuna geçerli şifre girer
        sendKey_utils(
            self.driver,
            passwordBox_Xpath,
            test_data.ly_password
        )

        # login butonuna tıklar
        click_utils(
            self.driver,
            loginButton_Xpath
        )





