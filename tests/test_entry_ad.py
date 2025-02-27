from pages.entry_ad_page import EntryAdPage
from pages.home_page import HomePage


def test_open_modal_window(driver):
    home_page = HomePage(driver)
    entry_ad_page = EntryAdPage(driver)
    home_page.click_page("Entry Ad")

    #  Verify if modal window is visible upon opening the page
    entry_ad_window_visibility = entry_ad_page.modal_window_visibility()

    assert entry_ad_window_visibility is True


def test_modal_window_message(driver):
    entry_ad_page = EntryAdPage(driver)

    #  Verify if modal window message match expected result
    message = entry_ad_page.get_modal_window_message()

    assert message == "It's commonly used to encourage a user to take an action " \
                      "(e.g., give their e-mail address to sign up for something or " \
                      "disable their ad blocker)."


def test_closing_modal_window(driver):
    entry_ad_page = EntryAdPage(driver)

    #  Verify if it is possible to close modal window
    entry_ad_page.click_close_window_button()
    ad_window_visibility = entry_ad_page.modal_window_visibility()

    assert ad_window_visibility is False


def test_re_enable_button(driver):
    entry_ad_page = EntryAdPage(driver)

    #  Verify if re-enable button opens modal window again
    entry_ad_page.click_re_enable_button()
    driver.refresh()
    ad_window_visibility = entry_ad_page.modal_window_visibility()

    assert ad_window_visibility is True
