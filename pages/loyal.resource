# loyal.resource
# C:\Users\user\PycharmProjects\exantring\pages\loyal.resource
# C:\Users\user\PycharmProjects\exantring\properties\test_data.py

# robot --include loginLoyalFriendCare C:\Users\user\PycharmProjects\exantring\Tests


*** Settings ***
Library         SeleniumLibrary
Library         String
Library         Collections
Library         ../utils/click_utils.py
Library         ../utils/sendkey_utils.py
Variables       ../properties/test_data.py
Library         ../utils/click_utils_robot.py
Library         ../utils/sendkey_utils_robot.py

*** Variables ***
${BROWSER}      chrome
${signinButton_Xpath}    (//*[@class="btn_add"])[1]
${emailBox_Xpath}    (//input[@id="email"])[1]
${passwordBox_Xpath}    (//input[@id="password"])[1]
${loginButton_Xpath}    //button[@class="btn btn-primary btn-cons m-t-10"]

# test_data.py dosyasından gelen değişkenleri burada tekrar isimlendiriyoruz todo
${ly_url}      ${ly_URL}
${userMail}    ${ly_mail}
${userPassword}    ${ly_password}

*** Keywords ***
Open Loyal Friend Care Home Page
    [Arguments]    ${ly_url}    ${browser}
    Open Browser  ${ly_url}    ${browser}
    Maximize Browser Window


Go To Login Page
    Smart Click Element    xpath=${signinButton_Xpath}

Login With Loyal Valid Data
    [Arguments]    ${mail}    ${password}
    Smart Send Keys    xpath=${emailBox_Xpath}    text=${ly_mail}
    Smart Send Keys    xpath=${passwordBox_Xpath}    text=${ly_password}
    Smart Click Element    xpath=${loginButton_Xpath}








