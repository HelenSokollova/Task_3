from .base_page import BasePage
from locators.personal_account_page_locators import *
import allure

class PersonalAccountPage(BasePage):
    @allure.step('Кликаем на кнопку История заказов')
    def click_button_orders_history(self):
        self.click(ORDERS_HISTORY)

    @allure.step('Кликаем на кнопку Выход')
    def click_button_exit(self):
        self.click_with_js(EXIT)
        