from selenium import webdriver
from selenium.webdriver.support.select import Select

driver= webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
cbs = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(cbs))

for cb in cbs:
    if cb.get_attribute("value") == "option3":
        cb.click()
        assert cb.is_selected()

rb = driver.find_elements_by_name("radioButton")
rb[1].click()

driver.get_screenshot_as_file("ss1.png")

ddwn = Select(driver.find_element_by_name("dropdown-class-example"))
ddwn.select_by_visible_text("Option3")
ddwn.select_by_index(1)

