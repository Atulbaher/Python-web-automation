# Selenium ?
# Selenium 3, 4 ?
# Selenium 3-> Selenium 4

# Selenium 3
# 1. you need to setup the Browse Drivers - Machine - PC/MAC
# 2. Problem - browser


# Selemium 4 ( most 70%)
# W3c - protocol, Selenium Manager - Which will automatically download the browser deiver for you

# QA -> Focus -> TEst case

from selenium import webdriver
import logging

def test_open_login():
    driver = webdriver.Chrome()
    LOGGER = logging.getLogger(__name__)
#Create a session with POST Request, (API POST Request)
# Fresh Chrome Browser will be open, Session ID is created.
#SessionId - 68614348f0cb4f521b963ed00eefbd0a
    driver.get("https://google.com")
    driver.maximize_window()
    LOGGER.info(driver.title)
    print("This is ATUL")


# 1 Session id -> close ID will be deleted
# Multiple windows in same session.
