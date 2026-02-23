*** Settings ***
Library    SeleniumLibrary
Resource   ../utils/sendkey_utils.py
Variables  ../properties/test_data.py

*** Variables ***
${BROWSER}      chrome
${GIRIS_YAP_BUTTON}      //*[@class="btn btn-success fw-bold shadow-sm px-4"]
${USERNAME_BOX}          (//input[@class="form-control border-start-0 rounded-end-3"])[1]
${PASSWORD_BOX}          (//input[@class="form-control border-start-0 rounded-end-3"])[2]
${SUBMIT_BUTTON}         //button[@class="btn btn-login w-100"]
${url}                   ${pv_lessons_url}
${username}              ${pv_lessons_userName}
${password}              ${pv_lessons_password}

*** Keywords ***
Open privateLessons Home Page
    Open Browser    ${url}    ${BROWSER}
    Maximize Browser Window

Login Method
    [Arguments]    ${username}    ${password}
    click_element     ${GIRIS_YAP_BUTTON}
    input_text    ${USERNAME_BOX}    ${username}
    input_text    ${PASSWORD_BOX}    ${password}
    click_element    ${SUBMIT_BUTTON}

*** Test Cases ***
Login to privateLessons
    [Documentation]    Test the login functionality of privateLessons
    [Tags]    login
    Open privateLessons Home Page
    Login Method    ${username}    ${password}
