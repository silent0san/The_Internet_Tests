from config.common_imports import *
from config.env_settings import BASE_URL
from pages.basic_auth_page import BasicAuthPage


@pytest.fixture(scope="module")
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()


def test_basic_auth_valid(driver):
    basic_auth_page = BasicAuthPage(driver)

    # Verify if valid credentials allow user to login
    basic_auth_page.test_valid_credentials()
    answer_passed = basic_auth_page.get_answer()
    assert answer_passed == "Congratulations! You must have the proper credentials."


def test_basic_auth_invalid(driver):
    basic_auth_page = BasicAuthPage(driver)

    # Verify if invalid credentials allow user to login
    basic_auth_page.test_invalid_credentials()
    answer_failed = basic_auth_page.is_login_failed()
    assert answer_failed
