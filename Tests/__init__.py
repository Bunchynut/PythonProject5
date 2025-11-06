from selene import browser,have,be
import pytest
import pyautogui
import time

from selene.support.conditions.be import visible


# def test_basic_auth_with_pytest():
#     browser.open("/basic_auth")
#     pyautogui.write("Kirill")
#     pyautogui.press("Tab")
#     pyautogui.write("12345")
#     pyautogui.press("Enter")
#
#     browser.open("/basic_auth")
#     pyautogui.press("Tab")
#     pyautogui.press("Tab")
#     pyautogui.press("Tab")
#     pyautogui.press("Enter")
#     browser.element("body").should(have.text("Not authorized"))
# def test_click():
#     browser.open("/add_remove_elements/")
#     browser.element('button[onclick="addElement()"]').click()
#     browser.all("#elements > button").should(have.size(1))
#     browser.quit()
#
#     browser.open("/add_remove_elements/")
#     for _ in range(3):
#         browser.element('button[onclick="addElement()"]').click()
#     browser.all("#elements > button").should(have.size(3))
#     browser.quit()
#
#     browser.open("/add_remove_elements/")
#     for _ in range(2):
#         browser.element('button[onclick="addElement()"]').click()
#     browser.all("#elements > button").should(have.size(2))
#     browser.element("#elements > button:nth-child(1)").click()
#     browser.all("#elements > button").should(have.size(1))
#     browser.quit()
#


def test_broken_images():
    browser.open("https://the-internet.herokuapp.com/broken_images")

    images = browser.all("img")

    broken_count = 0
    for img in images:
        if browser.driver.execute_script("return arguments[0].naturalWidth === 0;", img.locate()):
            broken_count += 1
    print(f"Количество сломанных {broken_count}")