# US003LoginWithMethod.robot
# C:\Users\user\PycharmProjects\robot_beta_UI\Tests\US003LoginWithMethod.robot

*** Settings ***
Documentation    US003 - Test case for successful login functionality.
Library          SeleniumLibrary
Library          Collections
Variables       ../properties/test_data.py
Resource        ../pages/py.resource

*** Variables ***
# test_data.py dosyasından gelen değişkenleri burada tekrar isimlendiriyoruz
${py_url}      ${pv_lessons_url}
${userName}    ${pv_lessons_userName}
${password}    ${pv_lessons_password}

*** Test Cases ***
PY001 TC01 Login test
    [Tags]    login21
    Open Private Lessons    ${py_url}    ${BROWSER}
    Go To giris Page
    Login With Valid Data    ${userName}    ${password}
    Sleep    10s
