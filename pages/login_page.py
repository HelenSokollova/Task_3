from .base_page import BasePage
from locators.login_page_locators import *
import allure

class LoginPage(BasePage):
    @allure.step('Кликаем на кнопку Восстановить пароль')
    def click_button_forgot_password(self):
        self.wait_element_visible(BUTTON_FORGOT_PASSWORD)
        self.click_with_js(BUTTON_FORGOT_PASSWORD)

    @allure.step('Кликаем на кнопку Конструктор')
    def click_button_constructor(self):
        self.wait_element_visible(BUTTON_CONSTRUCTOR)
        self.click_with_js(BUTTON_CONSTRUCTOR)

    @allure.step('Кликаем на кнопку Лента Заказов')
    def click_button_order_feed(self):
        self.wait_element_visible(BUTTON_ORDER_FEED)
        self.click_with_js(BUTTON_ORDER_FEED)
