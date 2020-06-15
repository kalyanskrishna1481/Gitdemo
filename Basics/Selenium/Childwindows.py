from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()
k = driver.window_handles[1]
driver.switch_to.window(k)
leftr = driver.find_element_by_xpath("//div[@class='example']//h3").text
driver.close()
print(leftr)
driver.switch_to.window(driver.window_handles[0])
reftr = driver.find_element_by_xpath("//div[@class='example']//h3").text
print(reftr)

