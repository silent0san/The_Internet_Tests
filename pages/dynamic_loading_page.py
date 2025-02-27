from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicLoadingPage:
    def __init__(self, driver):
        self.driver = driver
        self.example1_path = (By.CSS_SELECTOR, "#content > div > a:nth-child(5)")
        self.example2_path = (By.CSS_SELECTOR, "#content > div > a:nth-child(8)")
        self.start_button = (By.XPATH, "//*[@id='start']/button")
        self.button_reaction = (By.ID, "finish")

    def go_to_example1(self):
        self.driver.find_element(*self.example1_path).click()

    def go_to_example2(self):
        self.driver.find_element(*self.example2_path).click()

    def click_start_button(self):
        self.driver.find_element(*self.start_button).click()

    def get_rendered_button_reaction(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.button_reaction))
        return self.driver.find_element(*self.button_reaction).text

    def get_hidden_button_reaction(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.button_reaction))
        return self.driver.find_element(*self.button_reaction).text
