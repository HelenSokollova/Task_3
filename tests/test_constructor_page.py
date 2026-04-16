import pytest
from pages.constructor_page import ConstructorPage
from locators.constructor_page_locators import *
from urls import TestUrls
import allure
import data

class TestConstructorPage:
    @allure.title('Проверка перехода на страницу личного кабинета по кнопке Личный Кабинет')
    @allure.description('Проверяем соответствие урла страницы, открывающейся по клику на кнопку Личный Кабинет, заданному урлу')
    def test_correct_button_personal_accaunt_click(self, authorized_user):
        constructor_page = ConstructorPage(authorized_user)
        constructor_page.click_button_personal_account()
        constructor_page.wait_url_contains(data.personal_account_page_text)
        current_url = constructor_page.get_current_url()
        actual_url = TestUrls.personal_account_url
        assert current_url == actual_url

    @allure.title('Проверка открытия поп-апа с деталями ингредиента по клику на ингредиент')
    @allure.description('Проверяем наличие поп-апа с деталями ингредиента, открывающегося по клику на ингредиент')
    def test_correct_ingredient_click(self, ingredient_page):
        popup = ingredient_page.wait_popup_visible()
        assert popup.is_displayed()
        assert ingredient_page.get_popup_text() == data.popup_text


    @allure.title('Проверка закрытия поп-апа с деталями ингредиента по клику на крестик')
    @allure.description('Проверяем успешное закрытие поп-апа с деталями ингредиента по клику на крестик')
    def test_correct_popup_ingredient_close(self, ingredient_page):
        ingredient_page.wait_popup_visible()
        ingredient_page.click_button_close_popup()
        assert ingredient_page.is_popup_closed()

    
    @allure.title('Проверка увеличения каунтера ингредиента при добавлении ингредиента в конструктор')
    @allure.description('Параметризованный тест. Проверяем, что после перетаскивания булки счетчик = 2, ингредиента = 1')
    @pytest.mark.parametrize("ingredient_locator, expected_count", [
        (BUN, 2),
        (INGREDIENT, 1)
    ])
    def test_increasing_ingredient_counter_success(self, driver, ingredient_locator, expected_count):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_page(TestUrls.constructor_page_url)
        constructor_page.move_element(ingredient_locator)
        assert constructor_page.get_ingredient_counter(ingredient_locator) == expected_count


    @allure.title('Проверка создания заказа авторизованным пользователем')
    @allure.description('Проверяем успешное создание заказа для авторизованного пользователя')
    def test_create_order_by_authorized_user_success(self, authorized_user):
        constructor_page = ConstructorPage(authorized_user)
        constructor_page.movie_elements()
        constructor_page.click_button_create_order()
        popup = constructor_page.wait_popup_create_order_visible()
        order_id = constructor_page.get_order_id()
        assert popup.is_displayed()
        assert order_id != data.order_id_standart
        
