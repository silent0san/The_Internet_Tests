from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory


class AddRemoveElementsPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.add_button = (By.XPATH, "//button[@onclick='addElement()']")
        self.delete_buttons = (By.CLASS_NAME, "added-manually")

    def click_add_element(self):
        self.driver.find_element(*self.add_button).click()

    def get_delete_buttons(self):
        return self.driver.find_elements(*self.delete_buttons)

    def click_delete_button(self, index=0):
        delete_buttons = self.get_delete_buttons()
        if delete_buttons and index < len(delete_buttons):
            delete_buttons[index].click()
