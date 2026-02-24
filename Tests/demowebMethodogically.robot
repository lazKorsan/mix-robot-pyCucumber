# demowebMethodogically.robot
# C:\Users\user\PycharmProjects\exantring\Tests\demowebMethodogically.robot

*** Settings ***
Documentation    demowebMethodogically_TC01 Login Testi
Library          SeleniumLibrary
Library          Collections
Library         ../utils/click_utils_robot.py
Library         ../utils/sendkey_utils_robot.py
Resource    ../Tests/DM001LoginTest.robot

*** Test Cases ***
DemowebShop experimentallittitiy
demowebMethodogically login testi
Go to demoLogin Page
DemowebShop Login Method
