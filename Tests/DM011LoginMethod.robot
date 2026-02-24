# DM011LoginMethod.robot
# C:\Users\user\PycharmProjects\exantring\Tests\DM011LoginMethod.robot

*** Settings ***
Documentation    DemoWebShop Login Test Keywords
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
${demoweb_url}                  https://demowebshop.tricentis.com/

*** Keywords ***
Open Demoweb Shop
    Open Browser    ${demoweb_url}    ${BROWSER}
    Maximize Browser Window

Go to demoLogin Page
    Smart Click Element    xpath=${demoweb_loginButton_Xpath}

DemowebShop Login Method
    [Arguments]    ${email}    ${password}
    Smart Send Keys    xpath=${demoweb_emailBox_Xpath}    text=${email}
    Smart Send Keys    xpath=${demoweb_passwordBox_Xpath}  text=${password}
    Smart Click Element    xpath=${demoweb_loginButton_Xpath2}

Full Login Test
    [Arguments]    ${email}    ${password}
    Open Demoweb Shop
    Go to demoLogin Page
    DemowebShop Login Method    ${email}    ${password}