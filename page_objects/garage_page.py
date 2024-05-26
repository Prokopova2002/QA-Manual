from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class GaragePage(BasePage):
    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-primary']"
        ).click()


class AddCarModal(BasePage):

    def select_brand(self, car_brand_name: str):
        self._driver.find_element(By.XPATH, "//select[@id='addCarBrand']").send_keys(
            car_brand_name
        )

    def select_model(self, car_model_name: str):
        self._driver.find_element(By.XPATH, "//select[@id='addCarModel']").send_keys(
            car_model_name
        )

    def set_mileage(self, car_mileage):
        self._driver.find_element(By.XPATH, "//input[@id='addCarMileage']").send_keys(
            car_mileage
        )

    def click_add_car_button(self):
        self._driver.find_element(
            By.XPATH, "//div[@class='modal-content']//button[@class='btn btn=primary']"
        ).click()


class FuelExpense(BasePage):

    def click_add_fuel_expense_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='car_add-expense btn btn-success']"
        ).click()


class AddFuelExpense(BasePage):
    def set_number_of_liters(self, number_of_liters):
        self._driver.find_element(
            By.XPATH, "//input[@id['addExpenseLiters']"
        ).send_keys(number_of_liters)

    def set_total_cost(self, total_cost):
        self._driver.find_element(
            By.XPATH, "//input[@id='addExpenseTotalCost']"
        ).send_keys(total_cost)

    def click_add_button(self):
        self._driver.find_element(
            By.XPATH, "//button[@class='btn btn-primary']"
        ).click()


