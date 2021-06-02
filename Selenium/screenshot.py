import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://pypi.org/project/selenium/'
driver.get(url)

time.sleep(1)

driver.save_screenshot('screenshot.png')