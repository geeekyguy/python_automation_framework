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
    @mark.login_test_2
    @mark.smoke
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Login")
    @allure.title("Test to verify login with In Valid User Id")
    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.get_user_name().send_keys("Admin")
        login_page.get_password().send_keys("password")
        login_page.get_button().click()
        TestBase.verify_visibility_of_web_element(self, login_page.get_login_error())
        expected_text = "Invalid credentialseee"
        actual_text = login_page.get_login_error().text
        print(login_page.get_login_error().text)
        if expected_text != actual_text:
            logger.error(f"Expected text is {expected_text} but found is {actual_text}")
        else:
            logger.info(f"Expected text is {expected_text} and actual is {actual_text}")
        print("Test Completed")
