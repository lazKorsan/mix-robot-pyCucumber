*** Settings ***
Documentation    US003 - Test case for successful login functionality.
Library          SeleniumLibrary
Library          Collections
Variables       ../properties/test_data.py
Resource        ../pages/py.resource

*** Variables ***
${py_url}    ${pv_lessons_url}