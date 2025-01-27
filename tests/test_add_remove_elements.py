from pages.add_remove_elements_page import AddRemoveElementsPage
from pages.home_page import HomePage


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
