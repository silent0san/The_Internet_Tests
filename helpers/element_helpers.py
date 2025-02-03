from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class ElementHelpers:
    def __init__(self, driver):
        self.driver = driver

    def get_element_header(self, element):
        return element.find_element(By.TAG_NAME, "header").text

    def drag_element(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
