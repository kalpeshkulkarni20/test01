from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://www.verifiedmarketreports.com")
print(driver.title)
print(driver.current_url)
driver.get("https://www.verifiedmarketreports.com/reports")
driver.back()
driver.refresh()
driver.close()