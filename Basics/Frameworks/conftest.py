import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def baseframe(request):
    browser = request.config.getoption("browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser == "edge":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer.exe")
    #elif browser == "firefox":
        #print("firefox")
        #driver = webdriver.Firefox(executable_path="C:\\Users\\geckodriver.exe")

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
    yield
    driver.close()
