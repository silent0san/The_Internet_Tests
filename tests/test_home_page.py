from config.common_imports import *
from config.env_settings import BASE_URL


@pytest.fixture(scope="module")
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def test_add_remove_elements(driver):
    # Verify page title
    assert driver.title == "The Internet"
    # Verify page address
    assert driver.current_url == "https://the-internet.herokuapp.com/"
