import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://stackoverflow.com/users/login'
driver.get(url)
time.sleep(1)

driver.get('https://www.google.co.in/')
time.sleep(1)

driver.get('http://youtube.com/')
time.sleep(1);

driver.back()
time.sleep(1)

driver.forward()
time.sleep(1)

driver.refresh()
time.sleep(1)