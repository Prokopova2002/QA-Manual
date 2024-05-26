import time

from page_objects.garage_page import AddCarModal, AddFuelExpense
from page_objects.home_page import HomePage
from page_objects.registration_page import RegistrationPage


def test_sing_up(driver):
    home_page = HomePage(driver)

    home_page.open()
    home_page.click_sing_up_button()

    registration_page = RegistrationPage(driver)
    registration_page.enter_username("Taras")
    registration_page.enter_user_last_name("Shevchenko")
    registration_page.enter_email("tshevchenko22@gmail.com")
    registration_page.enter_password("Password123")
    registration_page.enter_repeat_password("Password123")
    registration_page.click_register_button()

    registration_page.assert_user_data("Taras Shevchenko")

    add_car_modal = AddCarModal(driver)
    add_car_modal.select_brand("Audi")
    add_car_modal.select_model("Q7")
    add_car_modal.set_mileage(10000)
    add_car_modal.click_add_car_button()

    add_fuel_expense = AddFuelExpense(driver)
    add_fuel_expense.set_number_of_liters(10)
    add_fuel_expense.set_total_cost(100)
    add_fuel_expense.click_add_button()
