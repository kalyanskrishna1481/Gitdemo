import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

act = ActionChains(driver)
webele = driver.find_element_by_id('mousehover')
act.move_to_element(webele).perform()
act.context_click(driver.find_element_by_xpath("//div[@class='left-align']//a[1]")).perform()
time.sleep(3)
driver.get_screenshot_as_file("actions.png")
#top = driver.find_element_by_xpath("//div[@class='left-align']//a[1]")
act.move_to_element(driver.find_element_by_xpath("//div[@class='left-align']//a[1]")).click().perform()


