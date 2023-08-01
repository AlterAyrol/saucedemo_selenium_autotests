from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Last_page(Base):

    url = 'https://www.saucedemo.com/checkout-step-two.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    title_word_locator = '//span[@class="title"]'
    finish_locator = '//button[@id="finish"]'


    # Getters

    def get_title_word_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_word_locator)))

    def get_finish_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_locator)))


    # Actions

    def click_finish_locator(self):
        print('Click checkout')
        self.get_finish_locator().click()



    def check_last_page_title_and_go_on(self):
        self.get_current_url()

        if self.driver.current_url == self.url:

            self.assert_title_word(title_word=self.get_title_word_locator(), expected_result='Checkout: Overview')
            self.click_finish_locator()


