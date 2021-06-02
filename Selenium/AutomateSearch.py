import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.co.in/')

time.sleep(4)


searchBox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchBox.send_keys("aupee karim")
searchBox.send_keys(Keys.ENTER)

time.sleep(4)

driver.quit()