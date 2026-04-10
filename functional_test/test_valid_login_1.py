import logging

import allure
from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.home_page import HomePage
from PageObject.login_page import LoginPage
from utility.TestBase import TestBase

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@allure.suite("Login Related Tests")
class TestSampleSelenium(TestBase):
    @mark.login_test_1
    @mark.smoke1
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("Login")
    @allure.title("Test to verify login with Valid User Id")
    def test_login(self):
        login_page = LoginPage(self.driver)
        logger.info("Browser launched & navigated to the URL")
        login_page.get_user_name().send_keys("Admin")
        logger.info("Entered User name")
        login_page.get_password().send_keys("admin123")
        logger.info("Entered password")
        login_page.get_button().click()
        logger.info("Clicked on Login button")
        home = HomePage(self.driver)
        TestBase.verify_visibility_of_web_element(self, home.get_dashboard())
        is_dashboard_available = home.get_dashboard().is_displayed()
        logger.info("Verify Dashboard")
        assert is_dashboard_available is True, "Login is not Success"
        print("Test Completed")

    @mark.login_test_1
    @mark.smoke
    @allure.story("Login")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Test to verify login failed attempt")
    def test_login_fail(self):
        logger.error("Login Attempt failed due to authentication")
        assert False
