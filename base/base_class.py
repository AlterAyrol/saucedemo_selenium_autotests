from datetime import datetime

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:

    def __init__(self, driver):
        self.driver = driver


    # Locators
    burger_menu_locator = '//button[@id="react-burger-menu-btn"]'
    logout_locator = '//a[@id="logout_sidebar_link"]'
    about_locator = '//a[@id="about_sidebar_link"]'


    # Getters
    def get_burger_menu_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu_locator)))

    def get_logout_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.logout_locator)))

    def get_about_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_locator)))



    # Actions

    @allure.step('Открывает меню меню')
    def click_burger_menu_locator(self):
        self.get_burger_menu_locator().click()

    @allure.step('Нажимает кнопку logout')
    def click_logout_locator(self):
        self.get_logout_locator().click()

    @allure.step('Нажимает кнопку "about"')
    def click_about_locator(self):
        self.get_about_locator().click()


    """Method to get current URL"""

    @allure.step('Получает текущий url')
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current URL: ' + get_url)
        return get_url


    """Method assert title word"""
    @allure.step('Проверка соответствия текста на странице')
    def assert_title_word(self, title_word, expected_result):
        print("Проверка соответствия текста на странице: " + expected_result)
        value_word = title_word.text
        assert value_word == expected_result
        print('Соответствие названия страницы пройдено')


    """Method screenshot"""
    def screenshot_saver(self):
        now_date = datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = 'screenshot' + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\lazar\\PycharmProjects\\SeleniumProject3\\screen\\' + screenshot_name)


    """Method asser url"""
    @allure.step('Проверка url')
    def asser_url(self, expected_result):
        get_url = self.driver.current_url
        print('Проверка url')
        assert get_url == expected_result
        print("Указана url нужной страницы")