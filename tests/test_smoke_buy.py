import time

from pages.loginpage import LoginPage
from pages.products_page import ProductPage
from pages.curt_page import Curt_page
from pages.your_information_page import Your_information_page
from pages.last_page import Last_page
from pages.finish_page import Finish_page


def test_select_product(web_browser):
    '''Смоук тест по покупке товара, оформлению почтового адреса и оформлению'''

    # user_login_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    user_login_list = ['standard_user']
    user_password = 'secret_sauce'

    driver = web_browser

    test_num = 0

    for user_login in user_login_list:
        test_num += 1
        print(f"Start smoke testing №{test_num} with login - {user_login}. Check buy life cycle ")

        login = LoginPage(driver=driver)
        login.authorization(login_name=user_login, login_password=user_password)

        time.sleep(1)
        product_page = ProductPage(driver=driver)
        product_page.add_first_product_and_go_to_curt(test_item=test_num)

        time.sleep(1)
        curt_page = Curt_page(driver=driver)
        curt_page.check_cart_and_go_on()

        time.sleep(1)
        your_information_page = Your_information_page(driver=driver)
        your_information_page.enter_data_and_go_on()

        time.sleep(1)
        last_page = Last_page(driver=driver)
        last_page.check_last_page_title_and_go_on()

        time.sleep(1)

        finish_page = Finish_page(driver=driver)
        finish_page.check_finish_page_title_and_go_out()

        time.sleep(2)

        driver.refresh()
