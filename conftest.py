import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    yield driver                                            #передаёт драйвер тесту
    driver.quit()


@pytest.fixture
def user_registration(driver):
    #Нажать кнопку «Вход и регистрация».
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    
    #Нажать кнопку «Нет аккаунта».
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()
    
    return driver


@pytest.fixture
def user_login(driver):  #авторизация под заранее созданным пользователем
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.LOGIN_AND_REGISTRATION_BUTTON)).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys('existed@gmail.com')
    driver.find_element(*locators.PASSWORD_INPUT).send_keys('1111')
    driver.find_element(*locators.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.USER_NAME))

    return driver