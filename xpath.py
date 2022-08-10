from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
driver.find_element_by_xpath("//input[@id='userName']").send_keys("kalpesh")
driver.find_element_by_xpath("//input[@id='userEmail']").send_keys("aasd@gmail.com")
driver.find_element_by_xpath("//textarea[@id='currentAddress']").send_keys("Address")
driver.find_element_by_xpath("//textarea[@id='permanentAddress']").send_keys("Padd")
driver.find_element_by_css_selector("#submit").click()


