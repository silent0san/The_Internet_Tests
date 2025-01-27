def test_page_title(driver):
    # Verify page title
    assert driver.title == "The Internet"


def test_page_address(driver):
    # Verify page address
    assert driver.current_url == "https://the-internet.herokuapp.com/"
