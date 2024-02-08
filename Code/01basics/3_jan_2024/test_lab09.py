import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome -> chrome option
# Edge -> Edge option
# Firefox -> Firefox option

def test_open_login():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com")

    mp_btn = driver.find_element(By.ID, "btn-make-appointment")
    mp_btn.click()

    print(driver.current_url)
    #Verification of the URL
    # asser

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login" , "Error wrong URL"

    # Custom attribute it is not id, name, class -> Custom Attribute -
    # student = "praveen" , roll=123, phone="233", placeholder="dasda"
    # data-qa="dasda" , testID="123"

    # <input
    # type="password"
    # class="form-control"
    # placeholder="Password"
    # student="praveen"
    # value=""
    # autocomplete="off">

    time.sleep(5)
    driver.close()
    driver.quit()