import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import Base


class ProductPage(Base):

    url = 'https://www.saucedemo.com/inventory.html'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    title_word_locator = '//span[@class="title"]'
    product_list_locators = [['name', 'name locator', 'price locator', 'add_item locator'],
                    ['Sauce Labs Backpack', '//button[@id="add-to-cart-sauce-labs-backpack"]'],
                    ['Sauce Labs Bike Light', '//button[@id="add-to-cart-sauce-labs-bike-light"]'],
                    ['Sauce Labs Bolt T-Shirt', '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'],
                    ['Sauce Labs Fleece Jacket', '//button[@id="add-to-cart-sauce-labs-fleece-jacket"]'],
                    ['Sauce Labs Onesie', '//button[@id="add-to-cart-sauce-labs-onesie"'],
                    ['Test.allTheThings() T-Shirt (Red)',
                     '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]'],
                    ]
    shopping_cart_link = '//a[@class="shopping_cart_link"]'



    # Getters

    def get_product_list_locator(self, test_item):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_list_locators[test_item][1])))

    def get_cart_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shopping_cart_link)))

    def get_title_word_locator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_word_locator)))


    # Actions

    @allure.step('Нажимает "Add to cart"')
    def click_add_product(self, test_item):
        self.get_product_list_locator(test_item).click()

    @allure.step('Нажимает на кнопку корзины')
    def click_cart_locator(self):
        self.get_cart_locator().click()


    @allure.step('Начат метод который кладёт указанный товар в корзину и переход в вкладку корзина')
    def add_first_product_and_go_to_curt(self, test_item):

        self.get_current_url()

        if self.driver.current_url == self.url:
            self.assert_title_word(title_word=self.get_title_word_locator(), expected_result='Products')
            self.click_add_product(test_item)
            time.sleep(1)
            self.click_cart_locator()

    @allure.step('Начат метод который открывает меню и переходит по ссылке about')
    def open_burger_menu_and_go_to_about(self):
        self.click_burger_menu_locator()
        time.sleep(1)
        self.click_about_locator()
        time.sleep(1)
        self.asser_url(expected_result='https://saucelabs.com/')