from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import time

from base.base_class import Base


class Login_page(Base):

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

    def input_user_name(self, user_name):
        print('Input login')
        self.get_user_name().send_keys(user_name)

    def clear_user_name(self, user_name):
        print('Clear login field')
        for _ in range(len(user_name)):
            time.sleep(0.01)
            self.get_user_name().send_keys(Keys.BACKSPACE)

    def clear_password(self, login_password):
        print('Clear password field\n')
        for _ in range(len(login_password)):
            time.sleep(0.01)
            self.get_password().send_keys(Keys.BACKSPACE)

    def input_password(self, password):
        print('Input password')
        self.get_password().send_keys(password)

    def click_login_button(self):
        print('Click login button')
        self.get_login_button().click()


    # Methods

    def authorization(self, login_name, login_password):
        print('Авторизация')

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



