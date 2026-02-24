# DM005LoginTest.robot
# C:\Users\user\PycharmProjects\exantring\Tests\DM005LoginTest.robot

*** Settings ***
Documentation    DemoWebShop_TC001 Login Testi
Library          SeleniumLibrary
Library          Collections
Library          ../utils/click_utils_robot.py
Library          ../utils/sendkey_utils_robot.py

*** Variables ***
${BROWSER}      chrome
${demoweb_loginButton_Xpath}    //*[@class="ico-login"]
${demoweb_emailBox_Xpath}       //*[@id="Email"]
${demoweb_passwordBox_Xpath}    //*[@id="Password"]
${demoweb_loginButton_Xpath2}   //input[@value="Log in"][1]
${demoweb_email}                lazKorsan190220262054@gmail.com
${demoweb_password}             Query.2026
${demoweb_url}                  https://demowebshop.tricentis.com/

*** Keywords ***
Open Demoweb Shop
    Open Browser    ${demoweb_url}    ${BROWSER}
    Maximize Browser Window

Go to demoLogin Page
    Smart Click Element    xpath=${demoweb_loginButton_Xpath}

DemowebShop Login Method
    Smart Send Keys    xpath=${demoweb_emailBox_Xpath}    text=${demoweb_email}
    Smart Send Keys    xpath=${demoweb_passwordBox_Xpath}  text=${demoweb_password}
    Smart Click Element    xpath=${demoweb_loginButton_Xpath2}

Full Login Test
    [Arguments]    ${email}    ${password}
    Open Demoweb Shop
    Go to demoLogin Page
    Smart Send Keys    xpath=${demoweb_emailBox_Xpath}    text=${email}
    Smart Send Keys    xpath=${demoweb_passwordBox_Xpath}  text=${password}
    Smart Click Element    xpath=${demoweb_loginButton_Xpath2}
