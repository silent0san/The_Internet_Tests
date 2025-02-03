from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Dropdown:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_menu = (By.ID, "dropdown")

    def get_dropdown_menu(self):
        return self.driver.find_element(*self.dropdown_menu)

    def get_list_item_count(self):
        select = Select(self.get_dropdown_menu())
        return len(select.options)

    def select_by_index(self, index):
        return self.dropdown_menu.select_by_index(index)

    def select_by_index(self, index):
        select = Select(self.get_dropdown_menu())
        select.select_by_index(index)

    #
    def get_selected_object(self):
        select = Select(self.get_dropdown_menu())
        return select.first_selected_option.text

