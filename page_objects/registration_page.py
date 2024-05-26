from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class RegistrationPage(BasePage):

    def enter_username(self, username: str):
        self._driver.find_element(By.XPATH, '//input[@id="singupName"]').send_keys(
            username
        )

    def enter_user_last_name(self, user_last_name: str):
        self._driver.find_element(By.XPATH, '//input[@id="singupLastName"]').send_keys(
            user_last_name
        )

    def enter_email(self, email: str):
        self._driver.find_element(By.XPATH, '//input[@id="singupEmail"]').send_keys(
            email
        )

    def enter_password(self, password: str):
        self._driver.find_element(By.XPATH, '//input[@id="singupPassword"]').send_keys(
            password
        )

    def enter_repeat_password(self, password: str):
        self._driver.find_element(
            By.XPATH, '//input[@id="singupRepeatPassword"]'
        ).send_keys(password)

    def click_register_button(self):
        self._driver.find_element(
            By.XPATH, '//button[@class="btn btn-primary"]'
        ).click()

    def assert_user_data(self, expected_user_data: str):
        user_data = self._driver.find_element(
            By.XPATH, '//p[@class="profile_name display-4"]'
        ).text
        assert user_data == expected_user_data


class DeletePage(BasePage):

    def click_remove_my_account_button(self):
        self._driver.find_element(
            By.XPATH, '//button[@class="btn btn-danger-bg"]'
        ).click()

    def click_remove_button(self):
        self._driver.find_element(By.XPATH, '//button[@class="btn btn-danger"]').click()
