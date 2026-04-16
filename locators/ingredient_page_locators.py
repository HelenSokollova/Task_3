from selenium.webdriver.common.by import By

POPUP_INGREDIENT = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")

POPUP_INGREDIENT_TEXT = (By.XPATH, "//*[text()='Детали ингредиента']")

CROSS_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__')]")
