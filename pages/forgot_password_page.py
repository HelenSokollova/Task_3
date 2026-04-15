from .base_page import BasePage
from locators.forgot_password_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains
import allure

class ForgotPasswordPage(BasePage):
    @allure.step('Заполняем поле Email')
    def fill_email_field(self, email):
        self.send_keys(EMAIL, email)
    
    @allure.step('Кликаем на кнопку Восстановить')
    def click_button_restore_password(self):
        self.wait_element_visible(BUTTON_RESTORE_PASSWORD)
        self.click_with_js(BUTTON_RESTORE_PASSWORD)

    @allure.step('Получаем текст поля формы восстановления пароля')
    def get_form_success(self):
        return self.get_text(FORM_SUCCESS)
    
    @allure.step('Кликаем на значок показать/скрыть пароль выбранное количество раз')
    def click_eye_icon(self, clicks=1):
        for _ in range(clicks):
            svg = self.find_element(EYE_BUTTON).find_element(*EYE_ICON)
            ActionChains(self.driver).move_to_element(svg).click().perform()

    @allure.step('Проверяем наличие подсветки поля ввода пароля')
    def is_password_field_highlighted(self):
        password_field = self.find_element(FIELD_HIGHLIGHT)
        class_attribute = password_field.get_attribute('class')
        return 'input_status_active' in class_attribute
    