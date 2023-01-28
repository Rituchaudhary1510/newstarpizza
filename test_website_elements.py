from selenium import webdriver
import allure
import pytest
from allure_commons.types import AttachmentType
import unittest
import json
import names
import time
import random
from random import randint
from selenium.webdriver.support.ui import Select
from methods import is_website_available, fetching_website
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class TestNewStarpizzabase(unittest.TestCase):

    def setUp(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(executable_path="C:/GitHub/BEST_IN_TOWN/chromedriver.exe", options=chrome_options)

        self.driver = webdriver.Chrome(
            "C:/Users/Digital Suppliers/Desktop/New_star_pizza/chromedriver.exe")

        f = open('data.json', "r")
        data = json.loads(f.read())
        fetching_website(self.driver, data["url"])
        f.close()

    def tearDown(self):
        self.driver.quit()


class TestWebsite(TestNewStarpizzabase):

    @allure.description("To verify that the website is available.")
    def test_01_website_availability(self):
        f = open("data.json", "r")
        data = json.loads(f.read())
        is_website_available(self.driver, data["url"])
        print("Test 01  ran successfully")
        f.close()

    @allure.description("To verify that the company logo is clearly visible")
    def test_02_logo_visibility(self):
        try:
            elem = self.driver.find_element_by_xpath(
                "/html/body/header[1]/div/div/div/div/div[1]/a/img")
            print(elem)
            if 'ng-hide' in elem.get_attribute('class'):
                print('Image is not visible on screen')
            else:
                allure.attach(self.driver.get_screenshot_as_png(
                ), name='logo_screen', attachment_type=AttachmentType.PNG)
                print('Image is visible on screen')
            print("Test 02  ran successfully")
        except Exception as ex:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_error_screen', attachment_type=AttachmentType.PNG)
            raise ex


if __name__ == '__main__':

    unittest.main()
