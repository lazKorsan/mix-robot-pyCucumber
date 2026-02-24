# DM012.robot
# C:\Users\user\PycharmProjects\exantring\Tests\DM012.robot

*** Settings ***
Resource    DM011LoginMethod.robot
Test Template    Full Login Test

*** Variables ***
${VALID_EMAIL}      lazKorsan190220262054@gmail.com
${VALID_PASSWORD}   Query.2026
${INVALID_EMAIL}    wrong@email.com
${INVALID_PASSWORD} wrongpass

*** Test Cases ***
Valid Login Test
    ${VALID_EMAIL}    ${VALID_PASSWORD}

Invalid Login Test - Wrong Password
    ${VALID_EMAIL}    ${INVALID_PASSWORD}

Invalid Login Test - Wrong Email
    ${INVALID_EMAIL}    ${VALID_PASSWORD}

Invalid Login Test - Both Wrong
    ${INVALID_EMAIL}    ${INVALID_PASSWORD}

Empty Email Test
    ${EMPTY}    ${VALID_PASSWORD}

Empty Password Test
    ${VALID_EMAIL}    ${EMPTY}

Empty Both Test
    ${EMPTY}    ${EMPTY}