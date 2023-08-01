import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Your_information_page(Base):

    url = 'https://www.saucedemo.com/checkout-step-one.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    title_word_locator = '//span[@class="title"]'
    first_name_locator = '//input[@id="first-name"]'
    last_name_locator = '//input[@id="last-name"]'
    zip_locator = '//input[@id="postal-code"]'
    continue_locator = '//input[@id="continue"]'


    # Getters

    def get_title_word_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_word_locator)))

    def get_first_name_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_locator)))

    def get_last_name_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_locator)))

    def get_zip_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_locator)))

    def get_continue_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_locator)))


    # Actions

    def input_first_name(self):
        print('Input first name')
        self.get_first_name_locator().send_keys('Qqq')

    def input_last_name(self):
        print('Input last name')
        self.get_last_name_locator().send_keys('Www')

    def input_zip(self):
        print('Input zip')
        self.get_zip_locator().send_keys('EEE')

    def click_continue_locator(self):
        print('Click continue')
        self.get_continue_locator().click()



    def enter_data_and_go_on(self):
        self.get_current_url()

        if self.driver.current_url == self.url:

            self.assert_title_word(title_word=self.get_title_word_locator(), expected_result='Checkout: Your Information')
            self.input_first_name()
            time.sleep(1)
            self.input_last_name()
            time.sleep(1)
            self.input_zip()
            time.sleep(1)
            self.click_continue_locator()





