# PS002Login.py
# C:\Users\user\PycharmProjects\exantring\practiceSoftWareTest\PS002Login.py


import self

from practiceSoftWareTest.PS001Login import navigate_to_practice_software_loginPage, practice_software_login, \
    practice_software_email, practice_software_password, navigate_home_page, practice_software_homePage


def test_practice_software_login():
    navigate_home_page()
    navigate_to_practice_software_loginPage(self)
    practice_software_login(self, practice_software_email, practice_software_password)


