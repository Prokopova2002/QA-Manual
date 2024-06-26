from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class HomePage(BasePage):
    def open(self):
        self._driver.get("https://guest:welcome2qauto@qauto.forstudy.space")

    def click_sing_up_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='hero-descriptor_btn btn btn-primary']"
        ).click()
