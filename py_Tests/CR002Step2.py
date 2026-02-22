

from pages.login_page import LoginPage
import properties.test_data as test_data

def test_create_courses_step2(driver):

    login_pg = LoginPage(driver)
    login_pg.navigate_to_login(test_data.login_url)
    login_pg.login_method(test_data.login_mail, test_data.instructor_password)
    #login_pg.navigate_to_new_courses()
    #login_pg.step1()
    driver.get("https://qa.instulearn.com/panel/webinars/3664/step/2")

    ########## todo step2 işlemleri ##########
