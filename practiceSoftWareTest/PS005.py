# PS005.py
# C:\Users\user\PycharmProjects\exantring\practiceSoftWareTest\PS005.py

import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.practice_software_pages import PracticeSoftwarePage, practice_software_homePage, practice_software_email, \
    practice_software_password


def test_practice_software_login(driver):
    page = PracticeSoftwarePage(driver)
    page.navigate_practice_software_homePage(practice_software_homePage)
    page.navigate_to_practice_software_loginPage()
    page.practice_software_login(practice_software_email, practice_software_password)
