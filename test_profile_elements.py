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
from methods import sign_in, edit_profile, add_delivery_address, get_homepage_using_profile_link, get_contactus_info, fetching_website, add_new_del_add
from methods import execute_click_by_product, select_product, select_combo_item, add_to_bag_and_verify_cart_details, Checkout_to_paymentscreen, place_ur_order_from_payment
from methods import remove_del_add, edit_del_add, add_new_card, remove_saved_card
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


class TestNewStarPizzaProfile(TestNewStarpizzabase):

    # @allure.description("To add delivery address.")
    # def test_01_add_delivery_address(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(5)
    #         sign_in(self.driver, data["username3"], data["password"])
    #         new_address = random.choice(data["addresslist"])
    #         hno = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
    #         add_delivery_address(self.driver, new_address)
    #         print("Test 01  ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify contact us link")
    # def test_02_verify_contactUs(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(3)
    #         sign_in(self.driver, data["username3"], data["password"])
    #         get_contactus_info(self.driver)
    #         print("Test 03 ran successfully")
    #     except Exception as ex:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise ex

    # @allure.description("To verify and add delivery address at checkout stage.")
    # def test_03_add_new_delivery_address_at_checkout(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         new_address = random.choice(data["addresslist"])
    #         hno = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
    #         sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["side_order"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         add_new_del_add(self.driver, new_address)
    #         # place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         print("Test case 03 ran successfully")
    #         # time.sleep(5)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify and remove a delivery address at checkout stage.")
    # def test_04_remove_delivery_address_at_checkout(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         new_address = random.choice(data["addresslist"])
    #         hno = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
    #         sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["side_order"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         remove_del_add(self.driver, new_address)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #     print("Test case 04 ran successfully")
    #     f.close()
    # except Exception as e:
    #     allure.attach(self.driver.get_screenshot_as_png(
    #     ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #     raise e

    # @allure.description("To verify and edit a delivery address at checkout stage.")
    # def test_05_edit_delivery_address_at_checkout(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         new_address = random.choice(data["addresslist"])
    #         hno = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
    #         sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["side_order"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         edit_del_add(self.driver, hno)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         print("Test case 05 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify and add new card details at checkout stage.")
    # def test_06_add_new_card_details_at_checkout(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         firstname = names.get_first_name()
    #         upercasename = firstname.upper()
    #         sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["side_order"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         add_new_card(self.driver, upercasename,
    #                      "4242424242424242", "12", "2024", "242")
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         print("Test case 06 ran successfully")
    #         # time.sleep(5)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    @allure.description("To verify and remove a card at checkout stage.")
    def test_07_remove_saved_card_at_checkout(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            new_address = random.choice(data["addresslist"])
            hno = ''.join(["{}".format(randint(0, 9)) for num in range(0, 2)])
            sign_in(self.driver, data["username3"], data["password"])
            for m in data["side_order"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                time.sleep(2)
                select_combo_item(self.driver, "Regular Crust")
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(self.driver)
            remove_saved_card(self.driver)
            place_ur_order_from_payment(self.driver, "Delivery")
            time.sleep(2)
            print("Test case 07 ran successfully")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e


if __name__ == '__main__':

    unittest.main()
