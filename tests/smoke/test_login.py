import pytest
import allure
from pages.login_page import LoginPage
from utils.read_test_data import TestDataReader

login_test_data = TestDataReader.get_json_data("login_test_data.json")


@allure.epic("Authentication")
@allure.feature("Login")
@pytest.mark.smoke
class TestLogin:

    @pytest.mark.parametrize("data", login_test_data)
    @allure.title("Verify invalid login")
    def test_invalid_login(self, driver, data):
        login_page = LoginPage(driver)

        with allure.step(f"Login with username: {data['username']}"):
            login_page.login(data["username"], data["password"])

        with allure.step("Validate error message"):
            actual_error = login_page.get_error_message()
            assert data["expected_error"] in actual_error