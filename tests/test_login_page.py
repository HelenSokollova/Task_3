from pages.login_page import LoginPage
from urls import TestUrls
import allure

class TestLoginPage:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке Восстановить пароль')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Восстановить пароль, заданному урлу')
    def test_correct_button_forgot_password_click(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(TestUrls.login_page_url)
        login_page.click_button_forgot_password()
        current_url = login_page.get_current_url()
        actual_url = TestUrls.forgot_password_url    
        assert current_url == actual_url

    @allure.title('Проверка перехода на страницу конструктора по кнопке Конструктор')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Конструктор, заданному урлу')
    def test_correct_button_constructor_click(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(TestUrls.login_page_url)
        login_page.click_button_constructor()
        current_url = login_page.get_current_url()
        actual_url = TestUrls.constructor_page_url   
        assert current_url == actual_url

    @allure.title('Проверка перехода на страницу ленты заказов по кнопке Лента Заказов')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Лента Заказов заданному урлу')
    def test_correct_button_order_feed_click(self, driver):
        login_page = LoginPage(driver)
        login_page.open_page(TestUrls.login_page_url)
        login_page.click_button_order_feed()
        current_url = login_page.get_current_url()
        actual_url = TestUrls.order_feed_url  
        assert current_url == actual_url
