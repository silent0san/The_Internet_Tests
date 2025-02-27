from pages.checkboxes_page import Checkboxes
from pages.home_page import HomePage


def test_total_checkboxes(driver):
    home_page = HomePage(driver)
    checkboxes_page = Checkboxes(driver)
    home_page.click_page("Checkboxes")

    #  Verify if quantity of checkboxes matches expected result
    total_checkboxes = len(checkboxes_page.get_checkboxes())
    assert total_checkboxes == 2


def test_checked_checkboxes(driver):
    checkboxes_page = Checkboxes(driver)

    #  Verify if quantity of checked checkboxes matches expected result
    checked_checkboxes = len(checkboxes_page.get_checked_checkboxes())
    assert checked_checkboxes == 1


def test_check_unchecked_checkboxes(driver):
    checkboxes_page = Checkboxes(driver)
    checkboxes_page.uncheck_checkboxes()

    #  Verify if unchecked checkboxes were checked
    unchecked_checkboxes = len(checkboxes_page.get_unchecked_checkboxes())
    assert unchecked_checkboxes == 2


def test_uncheck_checked_checkboxes(driver):
    checkboxes_page = Checkboxes(driver)
    checkboxes_page.check_checkboxes()

    #  Verify if checked checkboxes were unchecked
    checked_checkboxes = len(checkboxes_page.get_checked_checkboxes())
    assert checked_checkboxes == 2
