from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


#Login пользователя
class TestUserLogin:

    def test_user_login(self, user_login):
        #Проверить: произошёл переход на главную страницу, в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя и имя User.
        WebDriverWait(user_login, 5).until(expected_conditions.url_to_be('https://qa-desk.education-services.ru/login'))
        avatar = WebDriverWait(user_login, 5).until(expected_conditions.visibility_of_element_located(locators.USER_AVATAR))
        WebDriverWait(user_login, 5).until(expected_conditions.text_to_be_present_in_element(locators.USER_NAME, 'User.'))
    
        current_url = user_login.current_url
        current_name = user_login.find_element(*locators.USER_NAME).text
    
        assert current_url == 'https://qa-desk.education-services.ru/login'
        assert avatar.is_displayed()
        assert current_name == 'User.'
    