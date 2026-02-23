# py.resource
# C:\Users\user\PycharmProjects\exantring\pages\py.resource

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
${girisyapButton_Xpath}    //*[@class="btn btn-success fw-bold shadow-sm px-4"]
${usernameBox_Xpath}       (//input[@class="form-control border-start-0 rounded-end-3"])[1]
${passwordBox_Xpath}       (//input[@class="form-control border-start-0 rounded-end-3"])[2]
${submitButton_Xpath}      //button[@class="btn btn-login w-100"]

# test_data.py dosyasından gelen değişkenleri burada tekrar isimlendiriyoruz todo
${py_url}      ${pv_lessons_url}
${userName}    ${pv_lessons_userName}
${password}    ${pv_lessons_password}

*** Keywords ***
Open Private Lessons
    [Arguments]    ${url}    ${browser}
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

Go To giris Page
    # Kullanıcı login linkine basar
    ${status}=    Smart Click Element    xpath=${girisyapButton_Xpath}
    Should Be True    ${status}    Login Button'a tıklanamadı.

Login With Valid Data
    [Arguments]    ${name}    ${password}
    Smart Send Keys    xpath=${usernameBox_Xpath}    text=${name}
    Smart Send Keys    xpath=${passwordBox_Xpath}    text=${password}
    Smart Click Element    xpath=${submitButton_Xpath}
