# DW001LoginTest.py
# C:\Users\user\PycharmProjects\exantring\Demoweb\DW001LoginTest.py

from selenium import webdriver
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils


def test_demoweb_login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("https://demowebshop.tricentis.com/")

    demoweb_loginButton_Xpath='//*[@class="ico-login"]'
    click_utils(
        driver,
        demoweb_loginButton_Xpath
    )

    demoweb_emailBox_Xpath='//*[@id="Email"]'
    demoweb_passwordBox_Xpath='//*[@id="Password"]'
    demoweb_loginButton_Xpath='//input[@class="button-1 login-button"]'

    demoweb_email="lazKorsan190220262054@gmail.com"
    sendKey_utils(
        driver,
        demoweb_emailBox_Xpath,
        demoweb_email
    )

    demoweb_password="Query.2026"
    sendKey_utils(
        driver,
        demoweb_passwordBox_Xpath,
        demoweb_password
    )

    click_utils(
        driver,
        demoweb_loginButton_Xpath
    )

    driver.quit()



