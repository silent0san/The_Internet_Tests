from config.common_imports import *
from config.env_settings import BASE_URL
from pages.home_page import HomePage
from pages.add_remove_elements_page import AddRemoveElementsPage


@pytest.fixture(scope="module")
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


def test_add_remove_elements(driver):
    home_page = HomePage(driver)
    add_remove_elements_page = AddRemoveElementsPage(driver)

    home_page.click_page("Add/Remove Elements")

    # Verify if button "Add" adds "Delete" buttons
    add_remove_elements_page.click_add_element()
    delete_buttons = add_remove_elements_page.get_delete_buttons()
    assert len(delete_buttons) > 0

    # Verify if button "Delete" removes "Delete" button
    add_remove_elements_page.click_delete_button()
    delete_buttons = add_remove_elements_page.get_delete_buttons()
    assert len(delete_buttons) == 0
