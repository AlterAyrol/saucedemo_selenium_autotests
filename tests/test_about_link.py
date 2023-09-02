from selenium import webdriver
import time

from pages.loginpage import LoginPage
from pages.products_page import ProductPage


def test_about_link(web_browser):
    '''Смоук тест по переходу по ссылке about'''

    # user_login_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    user_login_list = ['standard_user']
    user_password = 'secret_sauce'

    driver = web_browser

    test_num = 0

    for user_login in user_login_list:
        test_num += 1
        print(f"Start smoke testing №{test_num} with login - {user_login}. Check about link")

        login = LoginPage(driver=driver)
        login.authorization(login_name=user_login, login_password=user_password)

        time.sleep(1)
        product_page = ProductPage(driver=driver)
        time.sleep(1)
        product_page.open_burger_menu_and_go_to_about()
