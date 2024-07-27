from selenium import webdriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--ignore-certificate-errors')

chrome = webdriver.Chrome(options=options)

try:
   chrome.get("http://uitestingplayground.com/classattr")

   for _ in range(3):
        blue_button_chrome = chrome.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        blue_button_chrome.click()
        sleep(2)

        chrome.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    chrome.quit()