from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class Checkboxes(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.checkboxes = (By.XPATH, "//input[@type='checkbox']")

    def get_checkboxes(self):
        checkboxes = self.driver.find_elements(*self.checkboxes)
        return checkboxes

    def get_checked_checkboxes(self):
        checkboxes = self.get_checkboxes()
        checked_checkboxes = [checkbox for checkbox in checkboxes if checkbox.is_selected()]
        return checked_checkboxes

    def get_unchecked_checkboxes(self):
        checkboxes = self.get_checkboxes()
        unchecked_checkboxes = [checkbox for checkbox in checkboxes if not checkbox.is_selected()]
        return unchecked_checkboxes

    def check_checkboxes(self):
        unchecked_checkboxes = self.get_unchecked_checkboxes()
        [checkbox.click() for checkbox in unchecked_checkboxes]

    def uncheck_checkboxes(self):
        checked_checkboxes = self.get_checked_checkboxes()
        [checkbox.click() for checkbox in checked_checkboxes]

