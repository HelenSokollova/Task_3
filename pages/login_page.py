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

    @allure.step('Заполняем поле email')
    def fill_email(self, email):
        self.find_element(INPUT_EMAIL).send_keys(email)
    
    @allure.step('Заполняем поле password')
    def fill_password(self, password):
        self.find_element(INPUT_PASSWORD).send_keys(password)

    @allure.step('Нажимаем кнопку Войти')
    def click_login_button(self):
        self.safe_click(BUTTON_LOGIN)
