import pytest
from selenium import webdriver
from dotenv import load_dotenv
import os
load_dotenv()


@pytest.fixture(scope="module")
def driver():
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=option)
    driver.get(os.getenv('BASE_URL'))
    yield driver
