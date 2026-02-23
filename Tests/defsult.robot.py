"""
import SeleniumLibrary
from robot.parsing.lexer.settings import Settings
from robot.parsing.model.statements import Setup
from setuptools.extension import Library

*** Settings ***
Library
SeleniumLibrary
Library
click_utils.RobotClickUtils

***Test Cases**
Buton
Tıklama
Testi
Circle
Options
color = blue
size = 25
[Setup]
Set
Driver    ${driver}

# Daire özelliklerini ayarla
Set

# Normal buton tıklama
Click Element   // button[ @ id = 'submit']    color = yellow

draw_circle = True

# Checkbox tıklama
Click
Checkbox // input[ @ type = 'checkbox']    draw_circle = True

# Metin ile tıklama
Click
Element
By
Text
Gönder
draw_circle = True

# Terms checkbox
Click
Terms
Checkbox
Keyword
draw_circle = True
"""