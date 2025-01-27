from pages.broken_images_page import BrokenImagesPage
from pages.home_page import HomePage


def test_broken_images(driver):
    home_page = HomePage(driver)
    broken_images_page = BrokenImagesPage(driver)
    home_page.click_page("Broken Images")

    #  Verify if quantity of broken images matches expected result
    total_broken_images = len(broken_images_page.get_images())
    assert total_broken_images == 2
