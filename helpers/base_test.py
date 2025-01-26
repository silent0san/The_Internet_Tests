import pytest
from selenium import webdriver
from config.env_settings import BASE_URL
from pages.basic_auth_page import BasicAuthPage


class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup_and_teardown(self, request):
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=option)
        self.driver.get(BASE_URL)
        # self.basic_auth_page = BasicAuthPage(self.driver)

        # Add finalizer to quit the driver after tests
        request.addfinalizer(self.driver.quit)
