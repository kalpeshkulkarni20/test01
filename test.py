import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service('C:\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://login.salesforce.com/?locale=in")



self.find_elements(by=By.CSS_SELECTOR, value="#username").click()
