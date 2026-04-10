import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = (Service("/Users/payzapp-automation/Documents/BrowserDriver/chromedriver-mac-x64/chromedriver"))
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.close()
