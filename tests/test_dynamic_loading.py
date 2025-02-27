from pages.dynamic_loading_page import DynamicLoadingPage
from pages.home_page import HomePage


def test_start_button_hidden(driver):
    home_page = HomePage(driver)
    dynamic_loading_page = DynamicLoadingPage(driver)
    home_page.click_page("Dynamic Loading")

    #  Verify if button returns correct value after loading
    dynamic_loading_page.go_to_example1()
    dynamic_loading_page.click_start_button()
    click_reaction = dynamic_loading_page.get_hidden_button_reaction()

    assert click_reaction == "Hello World!"


def test_start_button_rendered(driver):
    driver.back()
    dynamic_loading_page = DynamicLoadingPage(driver)

    #  Verify if button returns correct value after loading
    dynamic_loading_page.go_to_example2()
    dynamic_loading_page.click_start_button()
    click_reaction = dynamic_loading_page.get_rendered_button_reaction()

    assert click_reaction == "Hello World!"
