import pytest
from pages.order_list_page import OrderListPage
from locators.order_list_page_locators import *
from urls import TestUrls
import allure

class TestOrderListPage:
    @allure.title('Проверка открытия поп-апа с деталями заказа по клику на заказ в Ленте Заказов')
    @allure.description('Проверяем наличие поп-апа с деталями заказа, открывающегося по клику на заказ в Ленте Заказов')
    def test_correct_order_click(self, driver):
        order_list_page = OrderListPage(driver)
        order_list_page.open_page(TestUrls.order_feed_url)
        order_text = order_list_page.get_order_text()
        order_list_page.click_order_in_order_list()
        popup = order_list_page.wait_popup_visible()
        popup_text = order_list_page.get_popup_text()
        assert popup.is_displayed()
        assert order_text in popup_text


    @allure.title('Проверка увеличения счетчика при создании нового заказа')
    @allure.description('Проверяем увеличения счетчика Выполнено за все время и за сегодня при создании нового заказа')
    @pytest.mark.parametrize("counter_locator", [ALL_TIME_ORDERS,TODAY_ORDERS, ])
    def test_counter_increment(self, authorized_user, create_order_via_api, cancel_order_by_admin, counter_locator):
        order_list_page = OrderListPage(authorized_user)
        order_list_page.open_page(TestUrls.order_feed_url)
        initial_counter = order_list_page.get_counter_value(counter_locator)
        order_number = create_order_via_api()
        order_list_page.open_page(TestUrls.order_feed_url)
        updated_counter = order_list_page.get_counter_value(counter_locator)
        cancel_order_by_admin(order_number)
        assert updated_counter > initial_counter


    @allure.title('Проверка отображения заказа в "Ленте заказов" и в разделе "В работе"')
    @allure.description('Параметризованный тест. Проверяем, что созданный заказ отображается в "Ленте заказов" и в разделе "В работе"')
    @pytest.mark.parametrize("check_method", [
        "is_order_present",
        "is_order_in_work",
    ])
    def test_order_appears_in_sections(self, authorized_user, create_order_via_api, cancel_order_by_admin, check_method):
        order_list_page = OrderListPage(authorized_user)
        order_id = create_order_via_api()
        order_list_page.open_page(TestUrls.order_feed_url)
        assert getattr(order_list_page, check_method)(order_id)
        cancel_order_by_admin(order_id)
