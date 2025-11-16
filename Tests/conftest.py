from selene import browser
import pytest
import time

@pytest.fixture(autouse=True,scope='session')
def browser_management():
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
#