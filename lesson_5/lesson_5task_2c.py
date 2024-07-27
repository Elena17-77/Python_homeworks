from selenium import webdriver
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
chrome = webdriver.Chrome(options=options)

try:
    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")

    blue_button_chrome = chrome.find_element("xpath", '//button[text()="Button with Dynamic ID"]')

    for _ in range(3):
        blue_button_chrome.click()
        count = count + 1
        sleep(1)
        print(count)
except Exception as ex:
    print(ex)
finally:
    chrome.quit()