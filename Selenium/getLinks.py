import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/rekhabenatural/')

links = driver.find_elements_by_xpath("//*[@href]") #not #driver.find_element_by_xpath
for link in links:
    print(link.get_attribute('href'))

time.sleep(4)
