import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):

    url = 'https://www.saucedemo.com/checkout-complete.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    title_word_locator = '//span[@class="title"]'
    thank_you_locator = '//h2[@class="complete-header"]'


    # Getters

    def get_title_word_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_word_locator)))

    def get_thank_you_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.thank_you_locator)))


    # Actions

    @allure.step('Проверка тайтла страницы')
    def check_finish_page_title_and_go_out(self):
        self.get_current_url()

        if self.driver.current_url == self.url:

            self.assert_title_word(title_word=self.get_title_word_locator(), expected_result='Checkout: Complete!')
            self.assert_title_word(title_word=self.get_thank_you_locator(), expected_result='Thank you for your order!')

            self.click_burger_menu_locator()
            time.sleep(1)
            self.click_logout_locator()


