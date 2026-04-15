from selenium.webdriver.common.by import By

EMAIL = (By.CSS_SELECTOR, ".input__container input")

BUTTON_RESTORE_PASSWORD = (By.XPATH, "//*[text()='Восстановить']")

FORM_SUCCESS = (By.XPATH, "//*[text()='Пароль']")

EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")

EYE_ICON = (By.TAG_NAME, "svg")

FIELD_HIGHLIGHT = (By.XPATH, "//div[contains(@class, 'input_type_text')]")
