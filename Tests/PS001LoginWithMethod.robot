# PS001LoginWithMethod.robot
# C:\Users\user\PycharmProjects\exantring\Tests\PS001LoginWithMethod.robot

*** Settings ***
Documentation     Python Page Object Model yapısını kullanan Login Testi
Library           SeleniumLibrary

Library           pages.practice_software_pages.PracticeSoftwarePage

*** Test Cases ***
Login Test With Python Methods
    [Documentation]    Practice Software Testing sitesine Python metodları ile login testi.

    # Kullanici tarayiciyi açar
    Open Browser    about:blank    chrome
    Maximize Browser Window

    # Kullanici practicesoftware sayfasina gider
    Navigate To Practice Software Home Page

    # Kullanici login sayfasina gider
    Navigate To Practice Software Login Page

    # Kullanici login işlemlerini yapar
    Practice Software Login

    # Kullanici driver kapatir
    [Teardown]    Close Browser
