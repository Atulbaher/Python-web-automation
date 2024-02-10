import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_ebay_login():
    driver = webdriver.Chrome()
    driver.get("http:/ebay.com")

    assert driver.current_url == "https://www.ebay.com/"

    search_box =driver.find_element(By.XPATH,"//input[@id='gh-ac']")
    search_box.send_keys("16gb")

    search_btn = driver.find_element(By.XPATH,"//input[@id='gh-btn']")
    search_btn.click()

    lisr_result =driver.find_elements(By.XPATH,"//span[@role='heading']")
    for i in lisr_result:
        print(i.text)

    time.sleep(5)
    driver.quit()