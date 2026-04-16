from pages.personal_account_page import PersonalAccountPage
from urls import TestUrls
import allure
import data

class TestPersonalAccountPage:
    @allure.title('Проверка перехода на раздел История заказов личного кабинета по кнопке Истроия заказов')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку История заказов, заданному урлу')
    def test_correct_button_orders_history_click(self, user_in_personal_account):
        personal_account_page = PersonalAccountPage(user_in_personal_account)
        personal_account_page.click_button_orders_history()
        current_url = personal_account_page.get_current_url()
        actual_url = TestUrls.orders_history_url
        assert current_url == actual_url

    @allure.title('Проверка выхода из личного кабинета по кнопке Выход')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Выход, заданному урлу')
    def test_correct_button_exit_click(self, user_in_personal_account):
        personal_account_page = PersonalAccountPage(user_in_personal_account)
        personal_account_page.click_button_exit()
        personal_account_page.wait_url_contains(data.login_page_text)
        current_url = personal_account_page.get_current_url()
        actual_url = TestUrls.login_page_url
        assert current_url == actual_url
