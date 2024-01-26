import time

from selenium import webdriver


# Chrome -> Chrome Option
# Edge -> Edgr options
# Firefox -> Firefox Option

def test_open_login():
    chrome_option = webdriver.ChromeOptions()
    # Give some4 extra argument or extention or anything to chrome.
    # Chrome Option - Chrome with the Extention, Windows Size, Proxy, Js disabled

    extention_path = "/"
    extension_path = "/Users/pramod/Downloads/adblocker1x.crx"
    chrome_option.add_extension(extension_path)

    chrome_option.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_option)  # Fresh chrome which doesn't have anything
    driver.get("https://google.com")

    print(driver.title)
    time.sleep(2000)
