from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasicAuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.answer_div = (By.CSS_SELECTOR, "div.example")
        self.success_message = (By.CSS_SELECTOR, "div.example p")
        self.valid_user_name = "admin"
        self.valid_user_password = "admin"
        self.invalid_user_name = "user"
        self.invalid_user_password = "user"

    def test_valid_credentials(self):
        self.driver.get(
            f"https://{self.valid_user_name}:{self.valid_user_password}@the-internet.herokuapp.com/basic_auth")

    def test_invalid_credentials(self):
        self.driver.get(
            f"https://{self.invalid_user_name}:{self.invalid_user_password}@the-internet.herokuapp.com/basic_auth")

    def get_answer(self):
        try:
            element = self.driver.find_element(*self.success_message)
            return element.text
        except NoSuchElementException:
            return None

    def is_login_failed(self):
        answer = self.get_answer()
        return answer is None or "Congratulations! You must have the proper credentials." not in answer
