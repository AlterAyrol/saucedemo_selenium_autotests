from selenium import webdriver
import time

from pages.login_page import Login_page
from pages.products_page import Product_page
from pages.curt_page import Curt_page
from pages.your_information_page import Your_information_page
from pages.last_page import Last_page
from pages.finish_page import Finish_page



class Test():

    def test_about_link(self):
        '''Смоук тест по переходу по ссылке about'''

        # user_login_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
        user_login_list = ['standard_user']
        user_password = 'secret_sauce'

        driver = webdriver.Chrome()

        test_num = 0

        for user_login in user_login_list:
            test_num += 1
            print(f"Start smoke testing №{test_num} with login - {user_login}. Check about link")

            login = Login_page(driver=driver)
            login.authorization(login_name=user_login, login_password=user_password)

            time.sleep(1)
            product_page = Product_page(driver=driver)
            time.sleep(1)
            product_page.open_burger_menu_and_go_to_about()

            driver.close()


            time.sleep(2)
