from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class BrokenImagesPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.images = (By.TAG_NAME, "img")

    def get_images(self):
        images = self.driver.find_elements(*self.images)
        broken_images = []

        for img in images:
            src = img.get_attribute('src')
            if img.get_attribute('naturalWidth') == '0':
                broken_images.append(src)

        return broken_images
