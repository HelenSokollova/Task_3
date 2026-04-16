from .base_page import BasePage
from locators.order_list_page_locators import *
from selenium.webdriver.support.wait import WebDriverWait
import allure

class OrderListPage(BasePage):
    @allure.step('Получаем название заказа')
    def get_order_text(self):
        return self.get_text(ORDER_TEXT)
    
    @allure.step('Кликаем на заказ в ленте')
    def click_order_in_order_list(self):
        self.click(ORDER_TEXT)

    @allure.step('Дожидаемся загрузки поп-апа')
    def wait_popup_visible(self):
        popup = self.wait_element_visible(ORDER_POPUP)
        return popup
    
    @allure.step('Получаем текст поп-апа')
    def get_popup_text(self):
        return self.get_text(ORDER_POPUP_TEXT)
    
    
    @allure.step('Получаем значение счётчика: {counter_locator}')
    def get_counter_value(self, counter_locator):
        return self.get_text(counter_locator)
    
    @allure.step('Проверяем наличие заказа в "Ленте заказов"')
    def is_order_present(self, order_id, timeout=15):
        self.wait_for_text_in_elements(ORDER_NUMBERS_IN_FEED, f"#0{order_id}", timeout)
        return True

    @allure.step('Проверяем наличие заказа в разделе "В работе"')
    def is_order_in_work(self, order_id, timeout=15):
        self.wait_for_text_not_equal(ORDER_NUMBERS_IN_WORK, "Все текущие заказы готовы!", timeout)
        self.wait_for_text_in_elements(ORDER_NUMBERS_IN_WORK, str(order_id), timeout)
        return True
        