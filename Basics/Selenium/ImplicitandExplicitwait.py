import time


from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
itemslist = []
additem = []
drvr = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
drvr.maximize_window()
drvr.implicitly_wait(1)
drvr.get("https://rahulshettyacademy.com/seleniumPractise/#/")
drvr.find_element_by_css_selector("input.search-keyword").send_keys("ca")
time.sleep(1)

items = drvr.find_elements_by_xpath("//button[contains(text(),'ADD TO CART')]")
for item in items:
    itemslist.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    item.click()

print(itemslist)

drvr.find_element_by_css_selector("a.cart-icon").click()
drvr.find_element_by_xpath("//*[contains(text(),'PROCEED TO CHECKOUT')]").click()

addeditms = drvr.find_elements_by_css_selector("p.product-name")
for additems in addeditms:
    #additem.append(additems.text)
    if additems.text != "":
        additem.append(additems.text)

print(additem)

assert itemslist == additem

drvr.find_element_by_css_selector("input.promocode").send_keys("rahulshettyacademy")
drvr.find_element_by_xpath("//button[@class='promoBtn']").click()
wait = WebDriverWait(drvr, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
drvr.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()

country = Select(drvr.find_element_by_xpath("//div[@class='wrapperTwo']//div//select"))
country.select_by_visible_text("India")
drvr.find_element_by_css_selector("input.chkAgree").click()
drvr.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()

