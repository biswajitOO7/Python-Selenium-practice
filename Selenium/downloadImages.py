import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import wget

driver = webdriver.Chrome()
driver.get('https://en.wikipedia.org/wiki/Aupee_Karim')

time.sleep(2)

images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))
    imagesrc = image.get_attribute('src')
    os.system("wget "+ imagesrc + " -P img")
    #myfile = wget.download(imagesrc)

time.sleep(5)