from pages.context_menu_page import ContextMenu
from pages.home_page import HomePage


def test_context_menu(driver):
    home_page = HomePage(driver)
    context_menu_page = ContextMenu(driver)
    home_page.click_page("Context Menu")

    #  Verify if Context Menu is clickable and gives a valid message
    context_menu = context_menu_page.get_context_menu()
    context_menu_page.click_context_menu(context_menu)
    alert_text = context_menu_page.get_alert_window()

    assert alert_text == "You selected a context menu"

