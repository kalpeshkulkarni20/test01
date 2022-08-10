from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s=Service('C:\geckodriver.exe')
driver = webdriver.Firefox(service=s)



