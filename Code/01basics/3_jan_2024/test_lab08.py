import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome -> chrome option
# Edge -> Edge option
# Firefox -> Firefox option

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")

    #make_appointment_btn = driver.find_element(By.ID,"btn-make-appointment")
   # make_appointment_btn.click()

    #mp_btn = driver.find_element(By.PARTIAL_LINK_TEXT,"ment")
    #mp_btn.click()

    # # PARTIAL_LINK_TEXT
    # # Appointment
    # # Make Appointment
    # # Make
    # # App, ment

    # Link -> Full Exact Match
    # Partial -> Contains

   #mp_btn = driver.find_element(By.LINK_TEXT,"Make Appointment")
    #mp_btn.click()

    #mp_btn = driver.find_elements(By.CLASS_NAME,"btn.btn-dark.btn-lg")
    #mp_btn[1].click()

    mp_btn = driver.find_elements(By.TAG_NAME, "a")
    mp_btn[5].click()

    # Click on the Make App
    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    # <a
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>

    # ID - Unique ID
    # name, ClassName,
    # TagName -
    # Link/ partial
    # Css Selector
    # XPath

    # <input - Open Tag
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # > Close Tag


    time.sleep(5)
    driver.close()
    driver.quit()