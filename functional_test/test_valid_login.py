from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utility.TestBase import TestBase


class TestSampleSelenium(TestBase):
    @mark.login_test
    def test_login(self):
        user_name = self.driver.find_element(by=By.NAME, value="username")
        user_name.send_keys("Admin")
        password = self.driver.find_element(by=By.NAME, value="password")
        password.send_keys("admin123")
        login_button = self.driver.find_element(by=By.XPATH, value="//button[@type='submit']")
        login_button.click()
        home_page = self.driver.find_element(by=By.XPATH, value="//h6[text()='Dashboard']")
        is_dashboard_available = home_page.is_displayed()
        assert is_dashboard_available is True, "Login is not Success"
