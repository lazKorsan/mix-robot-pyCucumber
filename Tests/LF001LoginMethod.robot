# LF001LoginMethod.robot
# C:\Users\user\PycharmProjects\exantring\Tests\LF001LoginMethod.robot
# C:\Users\user\PycharmProjects\exantring\pages\loyal.resource



*** Settings ***
Documentation    LF001_TC01 - Test case for successful login functionality.
Library          SeleniumLibrary
Library          Collections
Variables       ../properties/test_data.py
Resource        ../pages/loyal.resource

*** Variables ***
# test_data.py dosyasından gelen değişkenleri burada tekrar isimlendiriyoruz todo
${ly_urlHome}    ${ly_URL}
${userMail}    ${ly_mail}
${userPassword}    ${ly_password}

*** Test Cases ***
LF001_TC001 Login To Loyal Friend Care Test
    [Tags]    loginLoyalFriendCare
    Open Loyal Friend Care Home Page    ${ly_urlHome}    ${BROWSER}
    Go To Login Page
    Login With Loyal Valid Data    ${userMail}    ${userPassword}




