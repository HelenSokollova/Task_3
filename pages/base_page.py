from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure
import data

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу')    
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Находим элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
    
    @allure.step('Кликаем по элементу')
    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step('Вводим текст в поле')
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    @allure.step('Ждем появления элемента')
    def wait_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ждем исчезновения элемента')
    def wait_element_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Скроллим к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    
    @allure.step('Кликаем через JavaScript')
    def click_with_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
        
    @allure.step('Ожидаем, что URL содержит текст "{text}"')
    def wait_url_contains(self, text):
        return WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(text))
    
    @allure.step('Ожидаем смену текста элемента')
    def wait_for_text_not_equal(self, locator, unwanted_text, timeout=10):
        custom_wait = WebDriverWait(self.driver, timeout)
        return custom_wait.until(lambda driver: driver.find_element(*locator).text if driver.find_element(*locator).text != unwanted_text else False)
    
    @allure.step('Перетаскиваем элемент через JavaScript')
    def _drag_and_drop_js(self, source, target):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);
                
                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source, target)


    @allure.step('Клик на элемент в зависимости от браузера')
    def safe_click(self, locator):
        element = self.find_element(locator)
    
        if data.driver_name == 'firefox':
            actions = ActionChains(self.driver)
            actions.move_to_element(element).pause(0.5).click().perform()
        else:
            element.click()    

    @allure.step('Находим все элементы по локатору')
    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)
    

    @allure.step('Ожидаем появления текста "{expected_text}" среди элементов')
    def wait_for_text_in_elements(self, locator, expected_text, timeout=30):
        WebDriverWait(self.driver, timeout).until(lambda driver: any(expected_text in element.text for element in driver.find_elements(*locator)))
        return self
    