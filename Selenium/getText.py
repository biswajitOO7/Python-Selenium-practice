import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://pypi.org/project/selenium/')

time.sleep(2)

elemnt = driver.find_element_by_xpath('//*[@id="description"]/h2')
print(elemnt.text)

driver.quit()