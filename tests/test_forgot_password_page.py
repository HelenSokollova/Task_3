import pytest
from pages.forgot_password_page import ForgotPasswordPage
import data
from urls import TestUrls
import allure

class TestLoginPage:
    @allure.title('Проверка перехода к форме ввода пароля и кода подтверждения по кнопке Восстановить')
    @allure.description('Проверяем соответствие формы, открывающейся по клику на кнопку Восстановить, заданному значению')
    def test_correct_button_restore_password_click(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(TestUrls.forgot_password_url)
        forgot_password_page.fill_email_field(data.email)
        forgot_password_page.click_button_restore_password()
        actual_text = forgot_password_page.get_form_success()
        assert data.restore_success in actual_text

    @allure.title('Проверка подсвечивания поля ввода пароля в форме ввода пароля при его восстановлении')
    @allure.description('Параметризованный тест. Проверяем наличие/отсутствие подсветки поля ввода пароля по клику на значок показать/скрыть пароль')
    @pytest.mark.parametrize('clicks, expected_highlight', [
    (1, True),
    (2, False)
])
    def test_password_field_highlighting_success(self, driver, clicks, expected_highlight):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_page(TestUrls.forgot_password_url)
        forgot_password_page.fill_email_field(data.email)
        forgot_password_page.click_button_restore_password()
        forgot_password_page.click_eye_icon(clicks)
        assert forgot_password_page.is_password_field_highlighted() == expected_highlight
      
  