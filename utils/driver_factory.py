from __future__ import annotations

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def _build_chrome_driver(options: ChromeOptions) -> webdriver.Chrome:
        """Create a Chrome driver with graceful fallback for offline environments."""
        try:
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options,
            )
        except Exception:
            # Fallback to Selenium Manager/system driver if webdriver-manager
            # cannot download binaries (common in restricted CI networks).
            return webdriver.Chrome(options=options)

    @staticmethod
    def _build_firefox_driver(options: FirefoxOptions) -> webdriver.Firefox:
        """Create a Firefox driver with graceful fallback for offline environments."""
        try:
            return webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options,
            )
        except Exception:
            return webdriver.Firefox(options=options)

    @staticmethod
    def get_driver(browser_name: str = "chrome", headless: bool = False):
        browser_name = browser_name.lower()

        try:
            if browser_name == "chrome":
                options = ChromeOptions()
                if headless:
                    options.add_argument("--headless=new")
                options.add_argument("--start-maximized")
                options.add_argument("--disable-notifications")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                return DriverFactory._build_chrome_driver(options)

            if browser_name == "firefox":
                options = FirefoxOptions()
                if headless:
                    options.add_argument("--headless")
                driver = DriverFactory._build_firefox_driver(options)
                driver.maximize_window()
                return driver

            raise ValueError(f"Unsupported browser: {browser_name}")
        except WebDriverException as exc:
            raise RuntimeError(
                "Unable to initialize browser driver. Ensure a compatible browser "
                "and driver are installed or available via Selenium Manager."
            ) from exc
