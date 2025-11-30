from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pytest
import time

@pytest.fixture(autouse=True, scope='session')
def browser_management():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.geolocation": 1
    })

    driver = webdriver.Chrome(options=chrome_options)
    browser.config.driver = driver
    browser.config.base_url = "https://the-internet.herokuapp.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6

    yield

    time.sleep(0.2)
    try:
        browser.quit()
    except Exception:
        pass

