import pytest
import requests
from selenium import webdriver
from pages.constructor_page import ConstructorPage
from pages.ingredient_page import IngredientPage
from pages.login_page import LoginPage
from urls import TestUrls
from helpers import generate_random_string
import data
import time


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        data.driver_name = 'chrome'
    else:
        driver = webdriver.Firefox()
        data.driver_name = 'firefox'
    yield driver
    
    driver.quit()


@pytest.fixture(scope='function')
def create_user_and_delete():
    user_email = f'{generate_random_string(10)}@gmail.com'
    user_password = generate_random_string(10)
    user_name = generate_random_string(10)
    
    user_data = {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }
    
    user_create = requests.post(f'{TestUrls.BASE_URL}{TestUrls.USERS_URL}register', json=user_data)
    token = None
    if user_create.status_code == 200:
        token = user_create.json().get('accessToken')
        user_data['token'] = token
    
    yield user_data  

    if token:
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        requests.delete(f'{TestUrls.BASE_URL}{TestUrls.USERS_URL}user', headers=headers)


@pytest.fixture(scope='function')
def authorized_user(driver, create_user_and_delete):
    user = create_user_and_delete
    login_page = LoginPage(driver)
    login_page.open_page(TestUrls.login_page_url)
    login_page.fill_email(user["email"])
    login_page.fill_password(user["password"])
    login_page.click_login_button()
    return driver


@pytest.fixture(scope='function')
def user_in_personal_account(authorized_user):
    constructor_page = ConstructorPage(authorized_user)
    constructor_page.click_button_personal_account()
    constructor_page.wait_url_contains(data.personal_account_page_text)  
    return authorized_user


@pytest.fixture(scope='function')
def ingredient_page(driver):
    constructor_page = ConstructorPage(driver)
    constructor_page.open_page(TestUrls.constructor_page_url)
    constructor_page.click_button_ingredient()
    constructor_page.wait_url_contains(data.ingredients_page_text)
    return IngredientPage(driver)


@pytest.fixture(scope='function')
def create_order_via_api(create_user_and_delete):
    def _create_order():
        token = create_user_and_delete['token']
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        response = requests.post(f'{TestUrls.BASE_URL}{TestUrls.ORDERS_URL}',headers=headers,json=data.ingredients_for_order)
        return response.json()['order']['number']
    return _create_order


@pytest.fixture(scope="session")
def admin_token():
    admin_email = f"admin_{int(time.time())}@test.ru"
    register_response = requests.post(f"{TestUrls.BASE_URL}{TestUrls.USERS_URL}register",
        json={
            "email": admin_email,
            "password": "admin123",
            "name": "Admin",
            "role": "admin"
        }
    )
    token = register_response.json().get('accessToken') 
    yield token

    if token:
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        requests.delete(f'{TestUrls.BASE_URL}{TestUrls.USERS_URL}user', headers=headers)


@pytest.fixture(scope='function')
def cancel_order_by_admin(admin_token):
    return lambda order_number: requests.get(f"{TestUrls.BASE_URL}{TestUrls.ORDERS_URL}?order={order_number}&cancel=true", headers={"Authorization": admin_token})
    