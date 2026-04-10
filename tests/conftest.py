import os
import pytest
import allure

from utils.driver_factory import DriverFactory
from utils.read_config import ConfigReader


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Environment name")
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")
    parser.addoption("--headless", action="store", default="false", help="Headless mode")


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return ConfigReader(env)


@pytest.fixture(scope="function")
def driver(request, config):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless").lower() == "true"

    driver = DriverFactory.get_driver(browser_name=browser, headless=headless)
    driver.implicitly_wait(config.get("implicit_wait", 5))
    driver.get(config.get("base_url"))

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            file_name = f"screenshots/{item.name}.png"
            driver.save_screenshot(file_name)

            allure.attach.file(
                file_name,
                name=item.name,
                attachment_type=allure.attachment_type.PNG
            )