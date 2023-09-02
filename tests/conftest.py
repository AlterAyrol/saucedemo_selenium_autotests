import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture()
def web_browser():

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    yield driver

    driver.close()

