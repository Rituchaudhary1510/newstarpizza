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
from selenium.webdriver.chrome.options import Options
from locators import checkoutlocators, productlocators
from methods import fetching_website, execute_click_by_product, select_product, sign_in, edit_profile, select_pizza
from methods import add_to_bag_and_verify_cart_details, Checkout_to_paymentscreen, sign_in2, Checkout, place_ur_order_from_payment
from methods import edit_items, delete_items_empty_cart, increase_item_in_cart, decrease_item_in_cart
from methods import logout, add_delivery_address, custom_tip, change_setting_to_delivery
from methods import fix_tip, find_element_by_text, delete_from_cart, empty_cart, checkout, select_burgers, select_beverages_cans, select_sandwichh_bread, select_wrap_extras, select_buffalo_wings, select_salad_dressing
from methods import select_card, select_dressings, is_website_available, order_setting, select_dressings
from methods import select_quantity, add_to_bag, sign_up, credit_card_payment, get_order_number, delivery_order_confirm_info
from methods import select_toppings, pickup_order_confirm_info, checkout2
from methods import select_card, asap_confirm_info, delete_card, invalid_signin, wrong_address, change_setting_to_pickup
from methods import review_details, later_order_setting, asap_setting, select_combo_item, verify_order_details


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


class TestNewStarPizzaMenu(TestNewStarpizzabase):

    # @allure.description("To verify pizza product can be added successfully to the cart.")
    # def test_01_pizza_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["pizza"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_pizza(self.driver, 'SM',
    #                          "Regular Crust ", "NO INSTRUCTIONS")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #             Checkout_to_paymentscreen(
    #                 self.driver, data["username3"], data["password"])
    #             time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify gourmet pizza product can be added successfully to the cart and then checkout.")
    # def test_02_gourmet_pizza_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["gourmet_pizza"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_pizza(self.driver, 'SM',
    #                          "Regular Crust ", "NO INSTRUCTIONS")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify stromboli product can be added successfully to the cart and then checkout to payment screen")
    # def test_03_stromboli_menu_item(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["stromboli"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_pizza(self.driver, 'SM',
    #                          "Regular Crust ", "NO INSTRUCTIONS")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify stromboli product can be added successfully to the cart and then checkout to payment screen")
    # def test_04_burger_menu_item(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["Burgers"]:
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_burgers(self.driver)
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify chicken over rice product can be added successfully to the cart and then checkout to payment screen")
    # def test_05_chicken_over_rice_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["Chicken_rice"]:
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_burgers(self.driver)
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         print("Test case 05 ran successfully")
    #         # time.sleep(5)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify desert product can be added successfully to the cart and then checkout to payment screen")
    # def test_06_dessert_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["desert"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         print("Test case 06 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify wing_ding product can be added successfully to the cart and then checkout to payment screen")
    # def test_07_verify_decrease_item_quantity_in_cart(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["wing_ding"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 07 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify FRIED CHICKEN PLATTERS product can be added successfully to the cart and then checkout to payment screen")
    # def test_08_verify_decrease_item_quantity_in_cart(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["Chicken_platters"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 08 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify chicken_nuggets product can be added successfully to the cart and then checkout to payment screen")
    # def test_09_chicken_nuggets_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["CHICKEN NUGGETS"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 09 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify chicken_fingers product can be added successfully to the cart and then checkout to payment screen")
    # def test_10_chicken_fingers_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["CHICKEN FINGERS"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 10 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify buffalo wings product can be added successfully to the cart and then checkout to payment screen")
    # def test_11_buffalo_wings_menu_item(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["BUFFALO WINGS"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_buffalo_wings(self.driver)
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify salads product can be added successfully to the cart and then checkout to payment screen")
    # def test_12_salads_menu_item(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["SALADS"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_salad_dressing(self.driver)
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify Pasta product can be added successfully to the cart and then checkout to payment screen")
    # def test_13_Pasta_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["PASTA"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 13 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify Seafood Platter product can be added successfully to the cart and then checkout to payment screen")
    # def test_14_Seafood_platter_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["SEAFOOD PLATTER"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 14 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify wraps product can be added successfully to the cart and then checkout to payment screen")
    # def test_15_wraps_menu_item(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["WRAPS"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_wrap_extras(self.driver)
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify Hoagies/Grind product can be added successfully to the cart and then checkout to payment screen")
    # def test_16_Hoagies_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["HOAGIES"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 16 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify Gyro product can be added successfully to the cart and then checkout to payment screen")
    # def test_17_Gyro_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["GYRO"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 17 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify hot and cold sandwich product can be added successfully to the cart and then checkout to payment screen")
    # def test_18_hot_cold_sandwich_menu_item(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["Hot_cold_sandwich"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_sandwichh_bread(self.driver)
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify Club sandwich product can be added successfully to the cart and then checkout to payment screen")
    # def test_19_Club_sandwich_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["Club_sandwich"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 17 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    @allure.description("To verify Grilled Chicken product can be added successfully to the cart and then checkout to payment screen")
    def test_20_grilled_chicken_stk_menuitem(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            # sign_in(self.driver, data["username3"], data["password"])
            for m in data["Grilled_chicken"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(
                self.driver, data["username3"], data["password"])
            print("Test case 20 ran successfully")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    # @allure.description("To verify Chicken Steaks product can be added successfully to the cart and then checkout to payment screen")
    # def test_21__chicken_stk_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["Chicken_steaks"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 21 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    @allure.description("To verify Beef Steaks product can be added successfully to the cart and then checkout to payment screen")
    def test_22_beef_stk_menuitem(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            # sign_in(self.driver, data["username3"], data["password"])
            for m in data["Beef_steaks"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                select_sandwichh_bread(self.driver)
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(
                self.driver, data["username3"], data["password"])
            print("Test case 22 ran successfully")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    # @allure.description("To verify QUESADILLA product can be added successfully to the cart and then checkout to payment screen")
    # def test_23_QUESADILLA_menuitem(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         time.sleep(2)
    #         # sign_in(self.driver, data["username3"], data["password"])
    #         for m in data["QUESADILLA"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(
    #             self.driver, data["username3"], data["password"])
    #         print("Test case 23 ran successfully")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    @allure.description("To verify Beverages product can be added successfully to the cart and then checkout to payment screen")
    def test_24_Beverages_menuitem(self):
        By_xpath = self.driver.find_element_by_xpath
        try:
            f = open("data.json", "r")
            data = json.loads(f.read())
            time.sleep(2)
            # sign_in(self.driver, data["username3"], data["password"])
            for m in data["Beverages"]:
                print(m)
                execute_click_by_product(self.driver, m)
                select_product(self.driver, m["menuitem"])
                select_beverages_cans(self.driver)
                add_to_bag_and_verify_cart_details(self.driver)
            Checkout_to_paymentscreen(
                self.driver, data["username3"], data["password"])
            print("Test case 24 ran successfully")
            f.close()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name='exception_screen', attachment_type=AttachmentType.PNG)
            raise e

    # @allure.description("To change order setting from Delivery to Pickup at checkout page.")
    # def test_08_Delivery_to_Pickup_order_setting(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         sign_in(self.driver, data["username3"], data["password"])
    #         time.sleep(2)
    #         for m in data["seafood_platters"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         time.sleep(3)
    #         order_setting(self.driver, "Pickup")
    #         place_ur_order_from_payment(self.driver, "Pickup")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To change order setting from Pickup to Delivery at checkout page.")
    # def test_09_Pickup_to_Delivery_order_setting(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         sign_in(self.driver, data["username3"], data["password"])
    #         time.sleep(2)
    #         order_setting(self.driver, "Pickup")
    #         for m in data["seafood_platters"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         time.sleep(3)
    #         order_setting(self.driver, "Delivery")
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e

    # @allure.description("To verify Recently placed order in order history.")
    # def test_13_Pickup_to_Delivery_order_setting(self):
    #     By_xpath = self.driver.find_element_by_xpath
    #     try:
    #         f = open("data.json", "r")
    #         data = json.loads(f.read())
    #         sign_in(self.driver, data["username3"], data["password"])
    #         time.sleep(2)
    #         for m in data["seafood_platters"]:
    #             print(m)
    #             execute_click_by_product(self.driver, m)
    #             select_product(self.driver, m["menuitem"])
    #             time.sleep(2)
    #             select_combo_item(self.driver, "Regular Crust")
    #             add_to_bag_and_verify_cart_details(self.driver)
    #         Checkout_to_paymentscreen(self.driver)
    #         time.sleep(3)
    #         place_ur_order_from_payment(self.driver, "Delivery")
    #         order_number = verify_order_details(
    #             self.driver, "Delivery", "9:30am")
    #         print(order_number)
    #         self.driver.get("https://bestintownpizzas.com/home")
    #         time.sleep(2)
    #         f.close()
    #     except Exception as e:
    #         allure.attach(self.driver.get_screenshot_as_png(
    #         ), name='exception_screen', attachment_type=AttachmentType.PNG)
    #         raise e


if __name__ == '__main__':

    unittest.main()
