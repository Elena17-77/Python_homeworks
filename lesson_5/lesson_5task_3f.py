from selenium import webdriver
from time import sleep
options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
firefox = webdriver.Firefox(options=options)

try:
   firefox.get("http://uitestingplayground.com/classattr")
   for _ in range(3):

        blue_button_firefox = firefox.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")

        blue_button_firefox.click()
        sleep(2)

        firefox.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    firefox.quit()