# PS004.py
# C:\Users\user\PycharmProjects\exantring\practiceSoftWareTest\PS004.py
# PracticeSoftwarePage
from pages.practice_software_pages import PracticeSoftwarePage, practice_software_email, practice_software_password


def test_practice_software_login(driver):
    practicesoftwarePage=PracticeSoftwarePage(driver)

    practicesoftwarePage.navigate_home_page()
    practicesoftwarePage.navigate_to_practice_software_loginPage()
    practicesoftwarePage.practice_software_login(practice_software_email, practice_software_password)

