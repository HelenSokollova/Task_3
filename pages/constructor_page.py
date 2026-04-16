from .base_page import BasePage
from locators.constructor_page_locators import *
from selenium.webdriver.common.action_chains import ActionChains
import data
import allure

class ConstructorPage(BasePage):
    @allure.step('Кликаем на кнопку Личный кабинет')
    def click_button_personal_account(self):
        self.safe_click(BUTTON_PERSONAL_ACCOUNT)


    @allure.step('Кликаем на ингредиент')
    def click_button_ingredient(self):
        self.scroll_to_element(INGREDIENT)
        self.click(INGREDIENT)


    @allure.step('Перетаскиваем булку и ингредиент компонент в область конструктора')
    def movie_elements(self):
        bun_element = self.find_element(BUN)
        ingredient_element = self.find_element(INGREDIENT)
        constructor_element = self.find_element(CONSTRUCTOR)
        if data.driver_name == 'firefox':
            self._drag_and_drop_js(bun_element, constructor_element)
            self._drag_and_drop_js(ingredient_element, constructor_element)
        else:
            ActionChains(self.driver).drag_and_drop(bun_element, constructor_element).perform()
            ActionChains(self.driver).drag_and_drop(ingredient_element, constructor_element).perform()


    @allure.step('Кликаем на кнопку Оформить заказ')
    def click_button_create_order(self):
        self.click(BUTTON_CREATE_ORDER)

    @allure.step('Дожидаемся загрузки поп-апа')
    def wait_popup_create_order_visible(self):
        popup = self.wait_element_visible(ORDER_CREATE_POPUP)
        return popup
        
    @allure.step('Ждем, пока номер заказа танет не 9999 и сменится на реальный номер)')
    def get_order_id(self):
        self.wait_popup_create_order_visible()
        return self.wait_for_text_not_equal(ORDER_ID, "9999")
    
    @allure.step('Получаем каунтер ингредиента')
    def get_ingredient_counter(self, ingredient_locator):
        ingredient = self.find_element(ingredient_locator)
        counter = ingredient.find_element(*INGREDIENT_COUNTER)
        return int(counter.text)
    
    @allure.step('Перетаскиваем элемент компонент в область конструктора')
    def move_element(self, ingredient_locator):
        element = self.find_element(ingredient_locator)
        constructor_element = self.find_element(CONSTRUCTOR)
    
        if data.driver_name == 'firefox':
            self._drag_and_drop_js(element, constructor_element)
        else:
            ActionChains(self.driver).drag_and_drop(element, constructor_element).perform()


    @allure.step('Кликаем на кнопку крестик')
    def close_order_popup(self):
        self.click(CLOSE_BUTTON)

   