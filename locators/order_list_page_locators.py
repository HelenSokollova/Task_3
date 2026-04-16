from selenium.webdriver.common.by import By

ORDER_TEXT = (By.XPATH, "//h2[contains(@class, 'text')]")

ORDER_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__')]")

ORDER_POPUP_TEXT = (By.XPATH, "//h2[contains(@class, 'text')]")

ALL_TIME_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")

TODAY_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')][1]")

ORDER_NUMBERS_IN_FEED = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list__')]")

ORDER_NUMBERS_IN_WORK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li")

