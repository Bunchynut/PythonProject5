from selene import browser,have,be,query
import openpyxl
import pytest
import pyautogui
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selene.support.conditions.be import visible
from selenium.webdriver.common.keys import Keys



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
#
#
#     browser.open("/add_remove_elements/")
#     for _ in range(3):
#         browser.element('button[onclick="addElement()"]').click()
#     browser.all("#elements > button").should(have.size(3))
#
#
#     browser.open("/add_remove_elements/")
#     for _ in range(2):
#         browser.element('button[onclick="addElement()"]').click()
#     browser.all("#elements > button").should(have.size(2))
#     browser.element("#elements > button:nth-child(1)").click()
#     browser.all("#elements > button").should(have.size(1))
#
#
# def test_broken_images():
#     browser.open("/broken_images")
#
#     images = browser.all("img")
#
#     broken_count = 0
#     for img in images:
#         if browser.driver.execute_script("return arguments[0].naturalWidth === 0;", img.locate()):
#             broken_count += 1
#     print(f"Количество сломанных {broken_count}")
# #
# def test_right_click():
#     browser.open("/context_menu")
#     element = browser.element('#hot-spot').should(be.visible)
#     actions = ActionChains(browser.driver)
#     actions.context_click(element()).perform()
#     alert = browser.switch_to.alert
#     assert alert.text == 'You selected a context menu'
#     alert.accept()
#     pyautogui.press('escape')
# def test_zahod():
#     browser.open("https://admin:admin@the-internet.herokuapp.com/digest_auth")
#
#     browser.element('body').should(have.text("Congratulations! You must have the proper credentials."))
#
#
# def test_propadaet():
#     browser.open("/disappearing_elements")
#     count = len(browser.all('ul li a'))
#     assert count >= 4
#
# def test_drag_and_drop():
#     browser.open('/drag_and_drop')
#     cubA = browser.element('#column-a')
#     cubB = browser.element('#column-b')
#     actions = ActionChains(browser.driver)
#     actions.drag_and_drop(cubA(), cubB()).perform()
#     browser.element('#column-a').should(have.text('B'))
#     browser.element('#column-b').should(have.text('A'))
#
# def test_dropdown():
#     browser.open("/dropdown")
#     browser.element('#dropdown').click()
#     browser.element('option:nth-child(2)').click()
#     browser.element('#dropdown').should(have.value('1'))
#     browser.element('#dropdown').click()
#     browser.element('option:nth-child(3)').click()
#     browser.element('#dropdown').should(have.value('2'))
#
# def test_dynamic_content():
#     browser.open('/dynamic_content')
#     browser.all('#content #content .row').should(have.size(3))
#     browser.all('#content #content img').should(have.size(3))
#     rows =  browser.all('#content #content .row')
#     for row in rows:
#         row.element('.large-10').should(have.text(' '))
#     broke_img = 0
#     imgs = browser.all('#content #content img')
#     for img in imgs:
#         is_broken = browser.driver.execute_script(
#             'return arguments[0].naturalWidth === 0;', img.locate())
#         if is_broken:
#             broke_img += 1
#     print(f'Кол-во битых {broke_img}')
#
# def test_entry_ad():
#     browser.open('/entry_ad')
#     browser.element('#modal > div.modal').wait_until(be.visible)
#     browser.element('#modal > div.modal > div.modal-footer > p').click()
#     browser.element('#restart-ad').click()
#     browser.element('#modal > div.modal').should(be.visible)
#
# def test_exit_intent():
#     browser.open('/exit_intent')
#     pyautogui.moveTo(50,50)
#     browser.element('#ouibounce-modal > div.modal').should(be.visible)
#     browser.element('#ouibounce-modal > div.modal > div.modal-footer > p').click()
#
# def test_floating_menu():
#     browser.open('/floating_menu#home')
#     browser.element('#menu').should(be.visible)
#     browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     browser.element('#menu').should(be.visible)
#
# def test_email():
#     browser.open('/forgot_password')
#     browser.element('#email').click()
#     pyautogui.write('Admin@mail.ru')
#     browser.element('#form_submit > i').click()
#     browser.element('body').should(have.text('Internal Server Error'))
#
# def test_login():
#     browser.open('/login')
#     browser.element('#username').click().type('Admin')
#     browser.element('#password').click().type('Admin')
#     browser.element('#login > button > i').click()
#     browser.element('#flash').should(be.visible)
#     browser.element('#flash').should(have.text('Your username is invalid!'))
#
#     browser.element('#username').click().type('tomsmith')
#     browser.element('#password').click().type('SuperSecretPassword!')
#     browser.element('#login > button > i').click()
#     browser.element('#flash').should(be.visible)
#     browser.element('#flash').should(have.text('You logged into a secure area!'))
#     browser.element('#content > div').should(have.text('Welcome to the Secure Area. When you are done click logout below.'))
#     browser.element('#content > div > a').click()
#
# def             \
#         test_nested_frames():
#     browser.open('/nested_frames')
#     browser.switch_to.frame(browser.element('[name="frame-top"]').locate())
#     browser.switch_to.frame(browser.element('[name="frame-left"]').locate())
#     browser.element('body').should(have.text('LEFT'))
#     browser.switch_to.default_content()
#
#     browser.switch_to.frame(browser.element('[name="frame-top"]').locate())
#     browser.switch_to.frame(browser.element('[name="frame-middle"]').locate())
#     browser.element('#content').should(have.text('MIDDLE'))
#     browser.switch_to.default_content()
#
#     browser.switch_to.frame(browser.element('[name="frame-top"]').locate())
#     browser.switch_to.frame(browser.element('[name="frame-right"]').locate())
#     browser.element('body').should(have.text('RIGHT'))
#     browser.switch_to.default_content()
#
#     browser.switch_to.frame(browser.element('[name="frame-bottom"]').locate())
#     browser.element('body').should(have.text('BOTTOM'))
#     browser.switch_to.default_content()
#
# def test_geolocation():
#     browser.open('/geolocation')
#     browser.element('#content > div > button').click()
#     browser.element('#lat-value').should(have.text('55.96213'))
#     browser.element('#long-value').should(have.text('37.4202334'))
#
# def test_horizontal_slider():
#     browser.open('/horizontal_slider')
#     actions = ActionChains(browser.driver)
#
#     browser.element('#content > div > div > input[type=range]').click()
#     for i in ['2.5', '3', '3.5', '4', '4.5', '5']:
#         browser.element('#range').should(have.text(i))
#         actions.send_keys(Keys.ARROW_RIGHT).perform()
#
#     for i in ['5', '4.5', '4', '3.5', '3', '2.5', '2', '1.5', '1', '0.5', '0']:
#         browser.element('#range').should(have.text(i))
#         actions.send_keys(Keys.ARROW_LEFT).perform()
#
# def hover(element):
#     actions = ActionChains(browser.driver)
#     actions.move_to_element(element.locate()).perform()
#
# def test_hovers():
#     browser.open("/hovers")
#
#     target = browser.element(".figure:nth-child(3)")
#     hover(target)
#     target.element(".figcaption").should(be.visible)
#
#     target = browser.element(".figure:nth-child(4)")
#     hover(target)
#     target.element(".figcaption").should(be.visible)
#
#     target = browser.element(".figure:nth-child(5)")
#     hover(target)
#     target.element(".figcaption").should(be.visible)
#
# def test_infinite_scroll():
#     browser.open('/infinite_scroll')
#     for _ in range(5):
#         browser.driver.execute_script("window.scrollBy(0, window.innerHeight);")
#         time.sleep(0.5)
#
#     browser.all('.jscroll-added').should(have.size_greater_than_or_equal(3))

def test_inputs():
    x = 0
    browser.open('/inputs')
    action = ActionChains(browser.driver)
    browser.element('#content > div > div > div > input[type=number]').click()
    for _ in range(10):
        x = x + 1
        action.send_keys(Keys.ARROW_UP).perform()
        browser.element('input[type=number]').should(have.value(str(x)))