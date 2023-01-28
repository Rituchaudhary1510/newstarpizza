import os
import time
import names
import json
import unittest
import allure
import pytest
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from methods import find_element_by_text
from methods import verify_order, edit_profile, edit_profile, logout, add_delivery_address, custom_tip, change_setting_to_delivery, fix_tip, find_element_by_text, delete_from_cart, empty_cart, new_card, pickup_order_setting, checkout, execute_click_by_text, select_card, select_dressings
from methods import is_website_available, order_setting, select_dressings, sign_in, select_quantity, add_to_bag, sign_up, credit_card_payment, get_order_number
from methods import delivery_order_confirm_info, select_toppings, pickup_order_confirm_info, checkout2, del_order_setting2, pickup_settings_2, edit_info, new_card, select_card
from methods import asap_confirm_info, delete_card, invalid_signin, wrong_address, change_setting_to_pickup, review_details, order_setting2, later_order_setting, asap_setting


class TestNewStarpizzaBase(unittest.TestCase):

    @allure.step("First Step to open the browser with title: {0}".format("Home"))
    def setUp(self):
        # user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/96.0.4664.55 Mobile/15E148 Safari/604.1"

        # _profile= webdriver.FirefoxProfile()
        # _profile.set_preference('general.useragent.override', user_agent)
        # self.driver= webdriver.Firefox(executable_path="/home/bnuser/TestScripts/geckodriver",firefox_profile=_profile)
        # self.driver.set_window_size(375, 812)
        # self.driver.implicitly_wait(5)
        # self.driver.get("https://qa-booknow.force.com/s/?site=a1L4K000000ZpKgUAK")
        # print("hit url")
        # print(self.driver.title)
        # time.sleep(5)

        s = 'C:/Users/Digital Suppliers/Desktop/New_star_pizza/chromedriver.exe'
        chrome_options = Options()
        chrome_options.add_argument(
            "user_agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/96.0.4664.110 Mobile/15E148 Safari/604.1")
        self.driver = webdriver.Chrome(
            options=chrome_options, executable_path=s)
        self.driver.set_window_size(375, 812)
        print("driver launched")
        self.driver.get("https://newstar.pizza/home")
        print("url hit")

    @allure.step("Close the browser")
    def tearDown(self):
        self.driver.quit()


class MobileViewTesting(TestBookNowBase):

    @allure.description("To verify that the website is available.")
    def test_01_website_availability(self):
        f = open("data.json", "r")
        data = json.loads(f.read())
        is_website_available(self.driver, data["url"])
        f.close()

    @allure.description("To verify that the company logo is clearly visible")
    def test_02_logo_visibility(self):
        try:
            elem = self.driver.find_element_by_xpath(
                "/html/body/header[2]/div/div/div/div/div[1]/div[3]/a/img")
            print(elem)
            if 'ng-hide' in elem.get_attribute('class'):
                print('Image is not visible on screen')
            else:
                allure.attach(self.driver.get_screenshot_as_png(
                ), name='logo_screen', attachment_type=AttachmentType.PNG)
                print('Image is visible on screen')

        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_error_screen', attachment_type=AttachmentType.PNG)
            raise ex

    @allure.description("To verify successful sign-in.")
    def test_03_signing_in(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username"], data["password"])
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e


if __name__ == '__main__':

    unittest.main()
