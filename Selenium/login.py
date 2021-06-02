import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'http://10.10.65.1/0/up/'
driver.get(url)

#emailField = driver.find_element_by_id('email')
emailField = driver.find_element_by_name('user')
emailField.send_keys('biswajitm_rss')

passwordField = driver.find_element_by_name('pass')
passwordField.send_keys('abc123')

loginButton = driver.find_element_by_name('login')
loginButton.click()

time.sleep(4)
driver.quit()