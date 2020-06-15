import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.switch_to.frame("courses-iframe")
time.sleep(10)
driver.find_element_by_link_text("Practice Projects").click()
driver.find_element_by_id("name").send_keys("kalyan")


