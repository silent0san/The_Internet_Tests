from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def click_page(self, page_name):
        self.driver.find_element(By.LINK_TEXT, page_name).click()
