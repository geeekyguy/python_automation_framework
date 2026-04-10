import allure
import pytest
from pages.login_page import LoginPage


@allure.epic("Authentication")
@allure.feature("Login")
@allure.story("Invalid Login")
@pytest.mark.smoke
@pytest.mark.login
class TestLogin:

    @allure.title("Verify user cannot login with invalid credentials")
    @allure.description("This test validates the error message for invalid login.")
    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)

        with allure.step("Login using invalid username and password"):
            login_page.login("wrong_user", "wrong_pass")

        with allure.step("Validate the error message"):
            assert "Invalid" in login_page.get_error_message()