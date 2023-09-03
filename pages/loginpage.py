import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time

from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    user_name = '//input[@id="user-name"]'
    password = '//input[@id="password"]'
    login_button = '//input[@id="login-button"]'



    # Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))



    # Actions

    @allure.step('Вводит имя пользователя')
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)

    @allure.step('Удаляет имя пользователя')
    def clear_user_name(self, user_name):
        for _ in range(len(user_name)):
            time.sleep(0.01)
            self.get_user_name().send_keys(Keys.BACKSPACE)

    @allure.step('Удаляет пароль')
    def clear_password(self, login_password):
        for _ in range(len(login_password)):
            time.sleep(0.01)
            self.get_password().send_keys(Keys.BACKSPACE)

    @allure.step('Вводит пароль')
    def input_password(self, password):
        self.get_password().send_keys(password)

    @allure.step('Нажимает кнопку "login"')
    def click_login_button(self):
        self.get_login_button().click()


    # Methods

    @allure.step('Начат метод авторизации')
    def authorization(self, login_name, login_password):

        self.driver.get(self.url)
        self.driver.maximize_window()

        self.get_current_url()
        self.input_user_name(login_name)
        self.input_password(login_password)
        time.sleep(1)
        self.click_login_button()

        if self.get_current_url() == self.url:
            print('Error in authorization. Try wait.')
            time.sleep(5)
            if self.driver.current_url == self.url:
                print('Error in authorization.\n')

                print('Очистка полей')
                self.clear_user_name(login_name)
                self.clear_password(login_password)



