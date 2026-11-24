import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestUserRegistration:
    
    #Регистрация пользователя
    def test_user_registration(self, user_registration):
        #Заполнить все поля формы регистрации и нажать кнопку «Создать аккаунт».
        new_email = f"some_email{random.randint(100,999)}@gmail.com"
        WebDriverWait(user_registration, 5).until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(new_email)
        user_registration.find_element(*locators.PASSWORD_INPUT).send_keys('1111')
        user_registration.find_element(*locators.SUBMIT_PASSWORD_INPUT).send_keys('1111')
        user_registration.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()
       
        #Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        WebDriverWait(user_registration, 5).until(expected_conditions.url_to_be('https://qa-desk.education-services.ru/regiatration'))
        avatar = WebDriverWait(user_registration, 5).until(expected_conditions.visibility_of_element_located(locators.USER_AVATAR))
        WebDriverWait(user_registration, 5).until(expected_conditions.text_to_be_present_in_element(locators.USER_NAME, 'User.'))

        current_url = user_registration.current_url
        current_name = user_registration.find_element(*locators.USER_NAME).text

        assert current_url == 'https://qa-desk.education-services.ru/regiatration'
        assert avatar.is_displayed()
        assert current_name == 'User.'

   #Регистрация пользователя c email не по маске  *******@*******.*** 
    def test_user_registration_invalid_email(self, user_registration):
        #Заполнить поле Email формы регистрации и нажать кнопку «Создать аккаунт». 
        WebDriverWait(user_registration, 5).until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys('invalid_email')
        user_registration.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()

        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        email = user_registration.find_element(*locators.EMAIL_ERROR_BORDER)
        password = user_registration.find_element(*locators.PASSWORD_ERROR_BORDER)
        submit_password = user_registration.find_element(*locators.SUBMIT_PASSWORD_ERROR_BORDER)

        expected_color = "rgba(255, 105, 114, 1)"

        error_message = WebDriverWait(user_registration, 5).until(expected_conditions.visibility_of_element_located(locators.FIELD_ERROR)).text

        for field in (email, password, submit_password):
            assert field.value_of_css_property("border-top-color") == expected_color
            assert field.value_of_css_property("border-bottom-color") == expected_color
            assert field.value_of_css_property("border-left-color") == expected_color
            assert field.value_of_css_property("border-right-color") == expected_color

        assert error_message == 'Ошибка'

    #Регистрация уже существующего пользователя
    def test_existed_user_registration(self, user_registration):
        #Заполнить все поля формы регистрации данными уже существующего в системе пользователя и нажать кнопку «Создать аккаунт».
        WebDriverWait(user_registration, 5).until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys('existed@gmail.com')
        user_registration.find_element(*locators.PASSWORD_INPUT).send_keys('1111')
        user_registration.find_element(*locators.SUBMIT_PASSWORD_INPUT).send_keys('1111')
        user_registration.find_element(*locators.CREATE_ACCOUNT_BUTTON).click()
        
        #Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным, под полем Email отображается сообщение «Ошибка».
        email = user_registration.find_element(*locators.EMAIL_ERROR_BORDER)
        password = user_registration.find_element(*locators.PASSWORD_ERROR_BORDER)
        submit_password = user_registration.find_element(*locators.SUBMIT_PASSWORD_ERROR_BORDER)
        
        expected_color = "rgba(255, 105, 114, 1)"
        
        error_message = WebDriverWait(user_registration, 5).until(expected_conditions.visibility_of_element_located(locators.FIELD_ERROR)).text
        
        for field in (email, password, submit_password):
            assert field.value_of_css_property("border-top-color") == expected_color
            assert field.value_of_css_property("border-bottom-color") == expected_color
            assert field.value_of_css_property("border-left-color") == expected_color
            assert field.value_of_css_property("border-right-color") == expected_color
        
        assert error_message == 'Ошибка'
