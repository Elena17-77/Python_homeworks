from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(service=FirefoxService(
GeckoDriverManager().install()))

driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/login')
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('tomsmith')
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('SuperSecretPassword!')
login_button = driver.find_element(By.CSS_SELECTOR, 'button.radius')
login_button.click()

sleep(2)
