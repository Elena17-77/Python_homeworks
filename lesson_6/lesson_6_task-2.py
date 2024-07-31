from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)


driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys('SkyPro')
driver.find_element(By.CSS_SELECTOR, '#updatingButton').click()
new_text = driver.find_element(By.CSS_SELECTOR, '#updatingButton').text
print(new_text)