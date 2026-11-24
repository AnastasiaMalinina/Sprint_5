import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


class TestCreateAdvertisment:

    #Создание объявления неавторизованным пользователем
    def test_create_ad_unauthorized_user(self, driver):
        #Нажать кнопку «Разместить объявление».
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.CREATE_ADVERTISMENT_BUTTON)).click()

        #Проверить: отображается модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь».
        modal_window = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.TO_POST_AN_AD_LOG_IN_WINDOW))
        assert modal_window.is_displayed()

    #Создание объявления авторизованным пользователем
    def test_create_ad_authorized_user(self, user_login):
        #Заполнить все поля формы: «Название», «Описание товара», «Стоимость» — стоимость должна быть указана в числовом формате.
        ad_name = f"Название{random.randint(1, 9999)}"
        WebDriverWait(user_login, 5).until(expected_conditions.element_to_be_clickable(locators.CREATE_ADVERTISMENT_BUTTON)).click()
        WebDriverWait(user_login, 5).until(expected_conditions.visibility_of_element_located(locators.AD_NAME_INPUT)).send_keys(ad_name)
        user_login.find_element(*locators.AD_DESCRIPTION_INPUT).send_keys(f"Описание{random.randint(1, 9999)}")
        user_login.find_element(*locators.AD_PRICE_INPUT).send_keys(random.randint(1, 9999))

        #Выбрать из Dropdown «Категорию» и «Город».
        user_login.find_element(*locators.AD_CATEGORY_DROPDOWN).click()
        WebDriverWait(user_login, 5).until(expected_conditions.element_to_be_clickable(locators.AD_CATEGORY_BOOKS)).click()
        user_login.find_element(*locators.AD_CITY_DROPDOWN).click()
        WebDriverWait(user_login, 5).until(expected_conditions.element_to_be_clickable(locators.AD_CITY_SPB)).click()

        #Выбрать RabioButton «Состояние товара».
        user_login.find_element(*locators.AD_RADIOBUTTON_CONDITION_USED).click()
        
        #Нажать кнопку «Опубликовать».
        user_login.find_element(*locators.AD_PUBLISH_BUTTON).click()

        #Перейти в профиль пользователя.
        WebDriverWait(user_login, 5).until(expected_conditions.visibility_of_element_located(locators.USER_AVATAR)).click()

        #Проверить: в блоке «Мои объявления» отображается созданное объявление.
        WebDriverWait(user_login, 5).until(expected_conditions.visibility_of_element_located(locators.MY_ADS_TITLE))
        my_ads = WebDriverWait(user_login, 5).until(expected_conditions.visibility_of_all_elements_located(locators.MY_AD_NAMES))

        ad_names = [ad.text for ad in my_ads]  #список текстовых названий объявлений

        assert ad_name in ad_names             #проверка наличия созданного объявления в списке объявлений
