import time
from selenium import webdriver

url = input("Enter url : ")
driver = webdriver.Chrome()

driver.get(url)

time.sleep(1)

for i in range(0,10):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)