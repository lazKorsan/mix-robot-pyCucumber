import time

import self
from selenium import webdriver

from pages.prvateLessonsPage import PrivateLessonsPage, girisyapButton_Xpath, usernameBox_Xpath, passwordBox_Xpath, \
    submitButton_Xpath
from properties import test_data
from utils.click_utils import click_utils
from utils.sendkey_utils import sendKey_utils


def test_homePage():
    # PrivateLessonsPage nesnesini oluştur
    pvPage=PrivateLessonsPage()

    # WebDriver'ı başlat
    pvPage.set_up()

    # Ana sayfaya git
    pvPage.navigate_to_homepage(test_data.pv_lessons_url)

    # navigate to login page
    click_utils(pvPage.driver, girisyapButton_Xpath)
    time.sleep(2)

    # userNmae box kutusuna geçerli kullanıcı adı girer
    sendKey_utils(
        pvPage.driver,
        usernameBox_Xpath,
        test_data.pv_lessons_userName
    )

    # password box kutusuna geçerli şifre girer
    sendKey_utils(
        pvPage.driver,
        passwordBox_Xpath,
        test_data.pv_lessons_password
    )

    # login butonuna tıklar
    click_utils(
        pvPage.driver,
        submitButton_Xpath
    )






