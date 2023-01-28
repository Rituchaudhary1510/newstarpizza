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
from locators import loginlocators
from methods import is_website_available, sign_in, invalid_signin, logout, sign_up, fetching_website, forget_password_link
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options


class TestNewStarpizzabase(unittest.TestCase):

    def setUp(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # self.driver = webdriver.Chrome(executable_path="C:/Users/Administrator/Desktop/BEST_IN_TOWN/chromedriver.exe", options=chrome_options)

        self.driver = webdriver.Chrome(
            "C:/Users/Digital Suppliers/Desktop/New_star_pizza/chromedriver.exe")
        f = open('data.json', "r")
        data = json.loads(f.read())
        fetching_website(self.driver, data["url"])
        f.close()

    def tearDown(self):
        self.driver.quit()


class TestNewStarPizzaLogin(TestNewStarpizzabase):

    # @allure.description("To verify successful sign-in.")
    # def test_01_signing_in(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(3)
    #         sign_in(self.driver, data["username3"], data["password"])
    #         print("Test 01 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify on entering incorrect password, correct error message is displaying.")
    # def test_02_negative_signin_with_wrong_password(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(5)
    #         invalid_signin(self.driver, data["username"], "abc1234")
    #         print("Test 02 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify on entering incorrect username, correct error message is displaying.")
    # def test_03_negative_signin_with_wrong_username(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(5)
    #         invalid_signin(self.driver, data["username3"], "12345678")
    #         print("Test 03 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    @allure.description("To verify account logout successfuly.")
    def test_04_logout(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(5)
            sign_in(self.driver, data["username3"], data["password"])
            logout(self.driver)
            print("Test 04 ran successfully")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    # @allure.description("To verify successful signup/new account.")
    # def test_05_signup(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         firstname = names.get_first_name()
    #         upercasename = firstname.upper()
    #         # lastname= names.get_last_name()
    #         # customername="{0}".format(firstname)
    #         # phone= ''.join(["{}".format(randint(0,9)) for num in range(0,10)])
    #         email = "{0}@gmail.com".format(firstname)
    #         password = "{0}@123456".format(firstname)
    #         time.sleep(5)
    #         sign_up(self.driver, upercasename, email, password, password)
    #         print("Test 05  ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify error messages with mismatch password while signup/new account.")
    # def test_06_signup_password_mismatch_error(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         firstname = names.get_first_name()
    #         upercasename = firstname.upper()
    #         email = "{0}@gmail.com".format(firstname)
    #         password = "{0}@1234".format(firstname)
    #         time.sleep(5)
    #         sign_up(self.driver, upercasename, email, password, "123456789")
    #         warning_msg = By_xpath(loginlocators.error_msg).text
    #         print(warning_msg)
    #         assert warning_msg == "The password confirmation does not match."
    #         print("Test 06 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify error messages when password less than minimum required value while signup/new account.")
    # def test_07_signup_insufficient_password_error(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         firstname = names.get_first_name()
    #         upercasename = firstname.upper()
    #         email = "{0}@gmail.com".format(firstname)
    #         password = "{0}@1234".format(firstname)
    #         time.sleep(5)
    #         sign_up(self.driver, upercasename, email, "12345", "12345")
    #         warning_msg = By_xpath(loginlocators.error_msg).text
    #         print(warning_msg)
    #         assert warning_msg == "The password must be at least 8 characters."

    #         print("Test 07 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify error messages when old email is used while signup/new account.")
    # def test_08_signup_old_email_taken_error(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         firstname = names.get_first_name()
    #         upercasename = firstname.upper()
    #         email = "{0}@gmail.com".format(firstname)
    #         password = "{0}@1234".format(firstname)
    #         time.sleep(5)
    #         sign_up(self.driver, upercasename,
    #                 "ritutanwar1510@gmail.com", password, password)
    #         warning_msg = By_xpath(loginlocators.error_msg).text
    #         print(warning_msg)
    #         assert warning_msg == "The email has already been taken."
    #         print("Test 08 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify that password reset link has been sent to the email.")
    # def test_09_forget_password_link(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(3)
    #         forget_password_link(self.driver, data["username3"])
    #         print("Test 09 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e


if __name__ == '__main__':

    unittest.main()
