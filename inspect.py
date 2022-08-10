from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service('C:\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//input[@name='email']").send_keys("kalpesh")

#driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("kalpesh@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("123456")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//body/app-root[1]/form-comp[1]/div[1]/form[1]/input[1]").click()

print(driver.find_element_by_class_name("alert-success").text)