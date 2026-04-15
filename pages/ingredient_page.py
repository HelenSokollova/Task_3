from .base_page import BasePage
from locators.ingredient_page_locators import *
import allure

class IngredientPage(BasePage):
    @allure.step('Дожидаемся загрузки поп-апа')
    def wait_popup_visible(self):
        popup = self.wait_element_visible(POPUP_INGREDIENT)
        return popup
    
    @allure.step('Получаем текст поп-апа')
    def get_popup_text(self):
        return self.get_text(POPUP_INGREDIENT_TEXT)
    
    
    @allure.step('Кликаем на кнопку крестик')
    def click_button_close_popup(self):
        self.click(CROSS_BUTTON)
    
    @allure.step('Проверяем, что поп-ап закрыт')
    def is_popup_closed(self):
        try:
            self.wait_element_invisible(POPUP_INGREDIENT)
            return True
        except:
            return False
        