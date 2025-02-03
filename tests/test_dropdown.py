from pages.dropdown_page import Dropdown
from pages.home_page import HomePage


def test_dropdown_default(driver):
    home_page = HomePage(driver)
    drag_and_drop_page = Dropdown(driver)
    home_page.click_page("Dropdown")

    selected_option = drag_and_drop_page.get_selected_object()

    #  Verify if default Dropdown Menu option is correct
    assert selected_option == "Please select an option"


def test_dropdown_select_option(driver):
    drag_and_drop_page = Dropdown(driver)

    selected_option_before = drag_and_drop_page.get_selected_object()
    drag_and_drop_page.select_by_index(1)

    selected_option_after = drag_and_drop_page.get_selected_object()

    #  Verify if it is possible to change Dropdown Menu selected option
    assert selected_option_before != selected_option_after


def test_dropdown_total_options(driver):
    drag_and_drop_page = Dropdown(driver)

    dropdown_count_elements = drag_and_drop_page.get_list_item_count()

    #  Verify if total amount of Dropdown Menu options is correct
    assert dropdown_count_elements == 3


def test_refresh_page_change_option(driver):
    drag_and_drop_page = Dropdown(driver)

    selected_option_before = drag_and_drop_page.get_selected_object()
    driver.refresh()

    selected_option_after = drag_and_drop_page.get_selected_object()

    #  Verify selected Dropdown Menu option will be the same after refreshing the page
    assert selected_option_before != selected_option_after
