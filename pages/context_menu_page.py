from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class ContextMenu:
    def __init__(self, driver):
        self.driver = driver
        self.context_menu = (By.ID, "hot-spot")
        self.alert_window = (By.LINK_TEXT, "You selected a context menu")

    def get_context_menu(self):
        context_menu = self.driver.find_element(*self.context_menu)
        return context_menu

    def click_context_menu(self, context_menu):
        ActionChains(self.driver).\
            context_click(context_menu).\
            perform()

    def get_alert_window(self):
        wait = WebDriverWait(self.driver, timeout=10)
        alert = wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text
