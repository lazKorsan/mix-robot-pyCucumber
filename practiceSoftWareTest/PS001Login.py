# PS001Login.py
# C:\Users\user\PycharmProjects\exantring\practiceSoftWareTest\PS001Login.py
import time

from selenium import webdriver
from robot.api.deco import keyword

from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils
practice_software_loginButton_Xpath='//*[@data-test="nav-sign-in"]'
practice_software_emailBox_Xpath='//input[@id="email"]'
practice_software_passwordBox_Xpath='//input[@id="password"]'
practice_software_loginButton_Xpath2='//input[@data-test="login-submit"]'
practice_software_homePage="https://practicesoftwaretesting.com/"
practice_software_email="lazKorsan@gmail.com"
practice_software_password = "Query.2026"


@keyword("Practice Software Login")
def navigate_home_page(url):
  # Kullanici practice software enginerring ana sayfasına gider
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.implicitly_wait(10)

  driver.get(url)

def navigate_to_practice_software_loginPage(driver):
  click_utils(
      driver,
      practice_software_loginButton_Xpath
  )
  time.sleep(2)

def practice_software_login(driver, mail, password):

  # mail adresini girer

  mail=practice_software_email
  sendKey_utils(
      driver,
      practice_software_emailBox_Xpath,
      mail
  )

  # şifreyi girer
  password=practice_software_password
  sendKey_utils(
      driver,
      practice_software_passwordBox_Xpath,
      password
  )
  # login butonuna tıklar
  click_utils(
      driver,
      practice_software_loginButton_Xpath2
  )




