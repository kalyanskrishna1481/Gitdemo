import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    print("welcome to conftest")


@pytest.fixture()
def chmesetup():
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://www.google.com/")
    driver.maximize_window()
    yield
    print(" I will execute last")
    driver.refresh()


@pytest.fixture(scope="class")
def tupleddata():
    print("here are the details")
    return["Kalyan", 1234.456,  "Krishna", "345"]


@pytest.fixture(scope="class")
def reports90():
    print("hello")
    return[1, 2, 3, 4, 5, 6, 7, 7]
