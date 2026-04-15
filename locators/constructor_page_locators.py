from selenium.webdriver.common.by import By

BUTTON_PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), 'Личный Кабинет')]")

INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')][4]")

BUN = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')][2]")

CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")

BUTTON_CREATE_ORDER = (By.XPATH, "//button[contains(@class, 'button_button')]")

ORDER_CREATE_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")

ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__')]")

INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class, 'counter_counter__num')]")

CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_')]")

