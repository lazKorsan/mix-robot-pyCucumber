# DM008.robot
*** Settings ***
Resource    DM007LoginTest.robot
Test Template    Full Login Test

*** Test Cases ***
Valid Login Test    ${demoweb_email}    ${demoweb_password}