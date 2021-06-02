import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://stackoverflow.com/users/login'
driver.get(url)

emailField = driver.find_element_by_id('email')
#emailField = driver.find_element_by_name('login')
emailField.send_keys('biswajit18at12@gmail.com')

passwordField = driver.find_element_by_id('password')
passwordField.send_keys('123')
#passwordField.send_keys(Keys.ENTER)

loginButton = driver.find_element_by_id('submit-button')
loginButton.click()

time.sleep(2)