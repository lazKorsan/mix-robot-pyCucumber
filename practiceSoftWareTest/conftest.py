import pytest
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.Driver import DriverManager

@pytest.fixture(scope="function")
def driver():

    driver = DriverManager.setup_driver(browser="chrome")
    
    yield driver
    

    if driver:
        driver.quit()
