from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EntryAdPage:
    def __init__(self, driver):
        self.driver = driver
        self.re_enable_button = (By.CSS_SELECTOR, "#restart-ad")
        self.modal_window = (By.CSS_SELECTOR, "#modal > div.modal")
        self.modal_window_message = (By.CSS_SELECTOR, "#modal > div.modal > div.modal-body > p")
        self.close_window_button = (By.CLASS_NAME, "modal-footer")

    def get_modal_window(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.modal_window))
        return self.driver.find_element(*self.modal_window)

    def get_modal_window_message(self):
        return self.driver.find_element(*self.modal_window_message).text

    def modal_window_visibility(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.modal_window))
            return self.get_modal_window().is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def click_close_window_button(self):
        self.driver.find_element(*self.close_window_button).click()

    def click_re_enable_button(self):
        self.driver.find_element(*self.re_enable_button).click()
