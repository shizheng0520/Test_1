import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config import url, driver_path

@pytest.fixture(scope = 'session')
def login():
    Service(executable_path = driver_path)
    driver = webdriver.Chrome(service = 0)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
