import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# XPath Functions
# XPath Axes
# CSS Selectors
# Alerts


def test_open_loging():
    driver = webdriver.Chrome()
    driver.get("http://app.vwo.com")

    #email_input = driver.find_element(By.XPATH,"//input[@id='login-username']")
    #password_input = driver.find_element(By.XPATH,"//input[@id='login-password']")
    #submit_input = driver.find_element(By.XPATH,"//button[@id='js-login-btn']")

    # By css selector

    email_input = driver.find_element(By.CSS_SELECTOR,"[id='login-username']")
    password_input = driver.find_element(By.CSS_SELECTOR,"[id='login-password']")
    submit_input = driver.find_element(By.CSS_SELECTOR,"[id='js-login-btn']")

    email_input.send_keys("admin")
    password_input.send_keys("admin")
    submit_input.click()


    time.sleep(5)
    driver.quit()
