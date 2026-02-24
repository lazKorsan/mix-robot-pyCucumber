# PS003Login.py
# C:\Users\user\PycharmProjects\exantring\practiceSoftWareTest\PS003Login.py
from selenium import webdriver

from practiceSoftWareTest.PS001Login import (
    navigate_to_practice_software_loginPage,
    practice_software_login,
    practice_software_email,
    practice_software_password,
    navigate_home_page, practice_software_homePage
)




def test_practice_software_login():
    # Web driver'ı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Ana sayfaya git
    navigate_home_page( practice_software_homePage)

    # Giriş sayfasına git
    navigate_to_practice_software_loginPage(driver)

    # Giriş yap
    practice_software_login(driver, practice_software_email, practice_software_password)

    # Browser'ı kapat
    driver.quit()
