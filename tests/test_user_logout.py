from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


#Logout пользователя
class TestUserLogout:

    def test_user_logout(self, user_login):
        #Нажать кнопку «Выйти»    
        WebDriverWait(user_login, 5).until(expected_conditions.element_to_be_clickable(locators.LOGOUT_BUTTON)).click()

        #Проверить: аватар пользователя и имя User больше не отображается в правом верхнем углу около кнопки «Разместить объявление», там теперь отображается кнопка «Вход и регистрация».
        assert WebDriverWait(user_login, 5).until(expected_conditions.invisibility_of_element_located(locators.USER_AVATAR))
        assert WebDriverWait(user_login, 5).until(expected_conditions.invisibility_of_element_located(locators.USER_NAME))
        assert WebDriverWait(user_login, 5).until(expected_conditions.visibility_of_element_located(locators.LOGIN_AND_REGISTRATION_BUTTON)).is_displayed()
    