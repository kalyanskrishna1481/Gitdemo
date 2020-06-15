import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//input[@minlength='2']").send_keys("Kalyan")

driver.find_element_by_xpath("//input[@name='email']").send_keys("krishna")

driver.find_element_by_css_selector("label[for='exampleCheck1']").click()


dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
driver.find_element_by_xpath("//*[@type='submit']").click()

checkmess = driver.find_element_by_xpath("//*[contains(text(),'Success!')]").text

assert "Success" in checkmess