from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def before_all(context):
    """
    Initializes the WebDriver before all tests run.
    It uses Selenium's built-in Selenium Manager to automatically handle the driver.
    """
    context.driver = None
    context.failed_to_initialize_driver = False
    try:
        print("Initializing WebDriver using Selenium Manager...")
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        
        # Selenium 4.6.0+ will automatically download and manage chromedriver
        context.driver = webdriver.Chrome(options=chrome_options)
        print("WebDriver initialized successfully.")

    except Exception as e:
        print(f"ERROR: Could not initialize WebDriver: {e}")
        print("This might be due to a network issue, firewall, or an incompatible Chrome version.")
        print("Please ensure you have a recent version of Selenium: 'pip install --upgrade selenium'")
        context.failed_to_initialize_driver = True

def after_all(context):
    """
    Quits the WebDriver after all tests have run.
    """
    if hasattr(context, 'driver') and context.driver:
        print("Quitting WebDriver.")
        context.driver.quit()
    elif context.failed_to_initialize_driver:
        print("WebDriver was not initialized, so no driver to quit.")
    else:
        print("No WebDriver instance was found in the context to quit.")

def before_step(context, step):
    """
    Checks if the driver failed to initialize before running each step.
    If it failed, the step is skipped.
    """
    if context.failed_to_initialize_driver:
        print(f"Skipping step due to WebDriver initialization failure: {step.name}")
        step.skip(reason="WebDriver initialization failed in before_all")
