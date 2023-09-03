import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Curt_page(Base):

    url = 'https://www.saucedemo.com/cart.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    title_word_locator = '//span[@class="title"]'
    checkout_locator = '//button[@id="checkout"]'


    # Getters

    def get_title_word_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_word_locator)))

    def get_checkout_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_locator)))


    # Actions

    @allure.step('Нажмает checkout')
    def click_checkout(self):
        self.get_checkout_locator().click()


    @allure.step('Проверка тайтла страницы')
    def check_cart_and_go_on(self):
        self.get_current_url()

        if self.driver.current_url == self.url:

            self.assert_title_word(title_word=self.get_title_word_locator(), expected_result='Your Cart')
            self.click_checkout()


