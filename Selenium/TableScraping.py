import time
from selenium import webdriver

driver = webdriver.Chrome()
#url = 'https://en.wikipedia.org/wiki/List_of_European_countries_by_GDP_growth'
url = 'https://tradingeconomics.com/country-list/gdp-annual-growth-rate?continent=europe'

driver.get(url)
time.sleep(1)

table = driver.find_element_by_xpath("//table[@class='table table-hover']")
for row in table.find_elements_by_xpath(".//tr"):
    for td in row.find_elements_by_xpath(".//td"):
        print(td.text),
    print("\n")