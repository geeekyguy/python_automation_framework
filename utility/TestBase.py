import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class TestBase:
    def verify_visibility_of_web_element(self, web_element):
        wait = WebDriverWait(self.driver, 15)
        wait.until(expected_conditions.visibility_of(web_element))

