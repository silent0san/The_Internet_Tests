from selenium.webdriver.common.by import By
from helpers.element_helpers import ElementHelpers


class DragAndDropPage:
    def __init__(self, driver):
        self.driver = driver
        self.source_element = (By.ID, "column-a")
        self.target_element = (By.ID, "column-b")
        self.element_helpers = ElementHelpers(driver)

    def get_source_element(self):
        return self.driver.find_element(*self.source_element)

    def get_target_element(self):
        return self.driver.find_element(*self.target_element)

    def get_source_element_header(self):
        return self.element_helpers.get_element_header(self.get_source_element())

    def drag_elements(self):
        self.element_helpers.drag_element(self.get_source_element(), self.get_target_element())
