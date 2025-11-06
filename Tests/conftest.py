from selene import browser
import pytest

@pytest.fixture(autouse=True)
def browser_management():
    browser.config.base_url = "https://the-internet.herokuapp.com"
    yield
    browser.quit()