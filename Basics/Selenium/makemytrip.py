from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.makemytrip.com/")

driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("rea")

