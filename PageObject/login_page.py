from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    user_name = (By.NAME, "username")

    def get_user_name(self):
        return self.driver.find_element(*LoginPage.user_name)

    password = (By.NAME, "password")

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    login_button = (By.XPATH, "//button[@type='submit']")

    def get_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    login_error = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")

    def get_login_error(self):
        return self.driver.find_element(*LoginPage.login_error)
