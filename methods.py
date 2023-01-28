from tkinter import E
from selenium import webdriver
import allure
import pytest
import time
import requests
import random
# import pytest_html
# import HtmlTestRunne
from selenium.webdriver.common.keys import Keys
from locators import loginlocators, productlocators, checkoutlocators, menugroupLocators, cartLocators, paymentLocators, placedPaymentLocators
from selenium.webdriver.support.ui import Select
from allure_commons.types import AttachmentType


@allure.step("To fetch the website with url: {1}")
def fetching_website(driver, site_url):
    try:
        driver.get(site_url)
        # driver.maximize_window()
        driver.set_window_size(1536, 864)
        driver.implicitly_wait(5)
        print(driver.title)
        allure.attach(driver.get_screenshot_as_png(),
                      name='website_screen', attachment_type=AttachmentType.PNG)
        try:
            driver.find_element_by_id(
                loginlocators.start_button).click()
        except:
            print("Restuarant has opened now")
        time.sleep(3)
        assert driver.title == "Home | New Star Pizza"

    except Exception as e:
        raise e


def find_element_by_text(driver, element_text):
    item = driver.find_element_by_xpath(
        "//*[contains(text(),'{}')]".format(element_text))
    return item


def find_element_by_text2(driver, element_text):
    item = driver.find_element_by_xpath(
        "//a[text()='{}']".format(element_text))
    return item


def execute_click_by_product(driver, itemlist):
    try:
        item = product_click(driver, itemlist["menugroup"])
        time.sleep(2)
    except Exception as e:
        raise e


def select_another_time(driver, timeslot):
    driver.find_element_by_id(
        loginlocators.another_time_button).click()
    time.sleep(3)
    driver.find_element_by_xpath(loginlocators.select_time).click()
    find_element_by_text(driver, "11:00 AM").click()
    time.sleep(2)
    driver.find_element_by_xpath(loginlocators.save_time_btn).click()


@allure.step("To perform click operation on the element specified in list:{1}")
def product_click(driver, productname):
    By_xpath = driver.find_element_by_xpath
    By_xpath_elements = driver.find_elements_by_xpath
    try:
        if productname == "Combo":
            By_xpath(menugroupLocators.combo).click()
        elif productname == "Pizza":
            By_xpath(menugroupLocators.pizza).click()
        elif productname == "Gourmet Pizza":
            By_xpath(menugroupLocators.gourmet_Pizza).click()
        elif(productname == "Stromboli"):
            By_xpath(menugroupLocators.strombolis).click()
        elif productname == "Burgers":
            By_xpath(menugroupLocators.burger).click()
        elif productname == "Chicken_over_rice":
            By_xpath(menugroupLocators.chicken_over_rice).click()
        elif productname == "DESERTS":
            By_xpath(menugroupLocators.desert).click()
        elif productname == "Wing_Ding":
            By_xpath(menugroupLocators.wing_ding).click()
        elif productname == "FRIED CHICKEN PLATTERS":
            By_xpath(menugroupLocators.fried_chicken_platter).click()
        elif productname == "CHICKEN NUGGETS":
            By_xpath(menugroupLocators.chicken_nuggets).click()
        elif productname == "CHICKEN FINGERS":
            By_xpath(menugroupLocators.chicken_fingers).click()
        elif productname == "BUFFALO WINGS":
            By_xpath(menugroupLocators.buffalo_wings).click()
        elif productname == "SALADS":
            By_xpath(menugroupLocators.salads).click()
        elif productname == "PASTA":
            By_xpath(menugroupLocators.pasta).click()
        elif productname == "SEAFOOD_PLATTER":
            By_xpath(menugroupLocators.seafood_platter).click()
        elif productname == "WRAPS":
            By_xpath(menugroupLocators.wraps).click()
        elif productname == "HOAGIES":
            By_xpath(menugroupLocators.hoagies).click()
        elif productname == "GYRO":
            By_xpath(menugroupLocators.gyro).click()
        elif productname == "HOT_COLD_SANDWICH":
            By_xpath(menugroupLocators.hot_cold_sandwiches).click()
        elif productname == "GRILLED_CHICKEN":
            By_xpath(menugroupLocators.grilled_chicken).click()
        elif productname == "CHICKEN_STEAKS":
            By_xpath(menugroupLocators.chicken_steaks).click()
        elif productname == "BEEF_STEAKS":
            By_xpath(menugroupLocators.beef_steaks).click()
        elif productname == "QUESADILLA":
            By_xpath(menugroupLocators.quesadilla).click()
        elif productname == "BEVERAGES":
            By_xpath(menugroupLocators.beverages).click()
        else:
            By_xpath(menugroupLocators.club_sandwiches).click()
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='exceptionerror_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select desired product")
def select_product(driver, productname):
    By_xpath = driver.find_element_by_xpath
    By_list_xpath = driver.find_elements_by_xpath
    try:
        print(productname)
        productname1 = productname.upper()
        product = find_element_by_text2(driver, productname)
        product.click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        print("product")
    except Exception as e:
        raise e


@allure.step("To be able to select desired product")
def select_combo_item(driver, size):
    By_xpath = driver.find_element_by_xpath
    By_list_xpath = driver.find_elements_by_xpath
    try:
        a = 0
        while(a < 6):
            try:
                find_element_by_text(driver, size).click()
                time.sleep(1)
            except:
                try:
                    driver.find_element_by_id(
                        productlocators.product_instruction).send_keys("No Pickels")
                except:
                    try:
                        driver.find_element_by_id(
                            productlocators.product_instructions).send_keys("No instructions")
                    except:
                        driver.find_element_by_id(
                            productlocators.product_instructions3).send_keys("Make it fast")
                time.sleep(1)
            try:
                find_element_by_text(driver, "Next").click()
            except:
                print("now add to bag")
                break
            time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        print("product")
    except Exception as e:
        raise e


@allure.step("To check website availability")
def is_website_available(driver, url):
    try:
        request_response = requests.head(url)
        status_code = request_response.status_code
        website_is_up = status_code == 200
        print("website_is_up")
        allure.attach(driver.get_screenshot_as_png(),
                      name='Website_screen', attachment_type=AttachmentType.PNG)
    except Exception as ex:
        raise ex


@allure.step("To create a new account")
def sign_up(driver, firstname, email, password, confirmpassword):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_xpath(loginlocators.signup_btn).click()
        time.sleep(2)
        By_id(loginlocators.signup_name).send_keys(firstname)
        By_id(loginlocators.signup_email).send_keys(email)
        By_id(loginlocators.signup_password).send_keys(password)
        By_id(loginlocators.signup_confirmPassword).send_keys(confirmpassword)
        By_xpath(loginlocators.register_btn).click()
        time.sleep(7)
        try:
            heading = By_xpath(loginlocators.home_signin_btn).text
            print(heading)
            assert firstname in heading
        except:
            print("error is there")
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Signup_failure_screen', attachment_type=AttachmentType.PNG)
        raise ex


@allure.step("To verify that user is able to sign in with any email id.")
def sign_in(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        time.sleep(4)
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(3)
        By_id(loginlocators.signin_email).send_keys(email)
        By_id(loginlocators.signin_password).send_keys(password)
        By_xpath(loginlocators.signin_btn).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        time.sleep(2)
        signed_in = By_xpath(loginlocators.signedin_label).text
        print(signed_in)
        assert signed_in in "RITU"
        return signed_in

    except Exception as e:
        raise e


@allure.step("To verify that user is able to sign in with Bestintown pizza account")
def forget_password_link(driver, email):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(1)
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_xpath(loginlocators.forget_password_btn).click()
        time.sleep(1)
        By_xpath(loginlocators.forget_password_email_field).send_keys(email)
        time.sleep(1)
        By_xpath(loginlocators.reset_link_btn).click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        success_msg = By_xpath(loginlocators.success_msg).text
        assert success_msg == "We have e-mailed your password reset link!"
        time.sleep(2)
    except Exception as e:
        raise e


@allure.step("To verify that user is able to sign in with Bestintown pizza account")
def sign_in2(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(1)
        By_xpath(loginlocators.signin_email).send_keys(email)
        By_xpath(loginlocators.signin_password).send_keys(password)
        By_xpath(loginlocators.signin_btn).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        time.sleep(2)
        # signed_in=By_xpath(loginlocators.signedin_label).text
        # print(signed_in)
        # assert signed_in in "SHARKTANK DEVELOPMENT"
        # return signed_in

    except Exception as e:
        raise e


@allure.step("To edit profile information")
def edit_profile(driver, name, email, name2):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(2)
        By_xpath(loginlocators.signedin_label).click()
        time.sleep(3)
        By_xpath(loginlocators.profile_btn).click()
        time.sleep(3)

        allure.attach(driver.get_screenshot_as_png(
        ), name='updated profile screen1', attachment_type=AttachmentType.PNG)
        time.sleep(2)
    except Exception as e:
        raise e


@allure.step("To add delivery address")
def add_delivery_address(driver, hno):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    By_name = driver.find_element_by_name
    try:
        time.sleep(2)
        By_xpath(loginlocators.signedin_label).click()
        time.sleep(3)
        By_xpath(loginlocators.del_add_link).click()
        time.sleep(4)
        By_xpath(loginlocators.add_new_address_btn).click()
        time.sleep(2)
        By_name(loginlocators.new_add_field).send_keys(hno)
        time.sleep(3)
        By_name(loginlocators.new_add_field).send_keys(Keys.DOWN)
        time.sleep(1)
        By_name(loginlocators.new_add_field).send_keys(Keys.ENTER)
        time.sleep(3)

        success_msg = By_xpath(loginlocators.address_add_message).text
        try:
            assert success_msg == "Good news! New Star Pizza can deliver to this address"
            By_xpath(loginlocators.save_add_btn).click()
            time.sleep(5)
            allure.attach(driver.get_screenshot_as_png(
            ), name='address_msg_screen', attachment_type=AttachmentType.PNG)
            try:
                warning_msg = By_xpath(loginlocators.warning_msg).text
                assert warning_msg == "The Address already exists."
                By_xpath(loginlocators.ok_btn).click()
                By_xpath(loginlocators.close_btn).click()
            except:
                print("new address has been added")
        except:
            assert success_msg == "New Star Pizza doesn't deliver to this address."
            By_xpath(loginlocators.close_btn).click()
            print("Doesn't delivery to your address")
        By_name(loginlocators.add_hno).send_keys("1322")
        allure.attach(driver.get_screenshot_as_png(
        ), name='new_updated_address', attachment_type=AttachmentType.PNG)
        time.sleep(2)
        # address_table = By_xpath(loginlocators.address_table).text
        # time.sleep(1)
        # assert hno in address_table
    except Exception as e:
        raise e


@allure.step("To login and then logout of the account")
def logout(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(3)
        By_xpath(loginlocators.logout_link).click()
        time.sleep(6)
        # label=By_xpath(loginlocators.home_signin_btn).text
        # assert label == "SIGN IN"
    except Exception as e:
        raise e


@allure.step("To verify that user is able to sign in withwrong credientials")
def invalid_signin(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(loginlocators.home_signin_btn).click()
        time.sleep(1)
        By_id(loginlocators.signin_email).send_keys(email)
        By_id(loginlocators.signin_password).send_keys(password)
        By_xpath(loginlocators.signin_btn).click()
        time.sleep(1)
        error = By_xpath(loginlocators.error_msg).text
        allure.attach(driver.get_screenshot_as_png(),
                      name='Signin_screen', attachment_type=AttachmentType.PNG)
        print(error)
        err_msg = "These credentials do not match our records."

        assert err_msg in error
    except Exception as e:
        raise e


@allure.step("To be able to select desired quantity")
def select_quantity(driver, quantity):
    try:
        By_xpath = driver.find_element_by_xpath
        try:
            By_xpath(productlocators.size).click()
        except:
            print("no size")
        time.sleep(2)
        try:
            By_xpath(productlocators.crust).click()
        except:
            print("no crust")
        time.sleep(2)
        # By_xpath(productlocators.quantity).clear()
        # By_xpath(productlocators.quantity).send_keys(quantity)
        # time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        print("quantity")
    except Exception as e:
        raise e


@allure.step("To be able to select pizza sides and quantity")
def select_pizza(driver, size, crust, instructions):
    By_xpath = driver.find_element_by_xpath
    try:
        try:
            if size == "SM":
                By_xpath(productlocators.pizza_small_size).click()
            elif size == "LG":
                By_xpath(productlocators.pizza_large_size).click()
            else:
                By_xpath(productlocators.pizza_Xlarge_size).click()
        except Exception as ex:
            raise ex
        try:
            find_element_by_text(driver, crust).click()
        except:
            print("no crust")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        By_xpath(productlocators.spinach_topping).click()
        time.sleep(1)
        By_xpath(productlocators.onion_topping).click()
        time.sleep(1)
        # By_xpath(productlocators.product_instruction).send_keys(instructions)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select burger topping and quantity")
def select_burgers(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        try:
            By_xpath(productlocators.cheese_path).click()
        except Exception as ex:
            raise ex
        time.sleep(1)

        By_xpath(productlocators.pickels_extras).click()
        time.sleep(1)
        By_xpath(productlocators.ketchup_extras).click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select buffalo wing size and sauces")
def select_buffalo_wings(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.wing_size).click()
        By_xpath(productlocators.BBQ_sauce).click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select salad different dressings")
def select_salad_dressing(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.ceaser_dressing).click()
        By_xpath(productlocators.italian_dressing).click()
        By_xpath(productlocators.vinegar_dressing).click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select wrap different dressings,extras and toppings")
def select_wrap_extras(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.extra_wrap).click()
        By_xpath(productlocators.sides_wrap).click()
        By_xpath(productlocators.salt_topping).click()
        time.sleep(1)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select sandwich bread")
def select_sandwichh_bread(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.white_bread).click()
        By_xpath(productlocators.ketchup_extras).click()

        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select beveerages")
def select_beverages_cans(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.cans_beverages).click()

        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        time.sleep(4)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To be able to select desired quantity")
def select_toppings(driver, quantity):
    try:
        By_xpath = driver.find_element_by_xpath
        try:
            By_xpath(productlocators.topping1).click()
        except:
            print("no size")
        time.sleep(2)
        try:
            By_xpath(productlocators.topping2).click()
        except:
            print("no crust")
        time.sleep(2)
        # By_xpath(productlocators.quantity).clear()
        # By_xpath(productlocators.quantity).send_keys(quantity)
        # time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        # print("quantity")
    except Exception as e:
        raise e


@allure.step("To be able to select desired quantity")
def select_dressings(driver, quantity):
    try:
        By_xpath = driver.find_element_by_xpath
        try:
            By_xpath(productlocators.dressing).click()
        except:
            print("no size")
        time.sleep(2)
        try:
            By_xpath(productlocators.extra_topping).click()
        except:
            print("no crust")
        time.sleep(2)
        # By_xpath(productlocators.quantity).clear()
        # By_xpath(productlocators.quantity).send_keys(quantity)
        # time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='toppings_screen', attachment_type=AttachmentType.PNG)
        # print("quantity")
    except Exception as e:
        raise e


@allure.step("to add product to bag")
def add_to_bag(driver, item):
    By_xpath = driver.find_element_by_xpath
    try:
        # By_xpath(productlocators.special_inst).send_keys("Extra cheese")
        time.sleep(2)
        By_xpath(productlocators.add_to_bag).click()
        time.sleep(2)
        print("added to bag")
        allure.attach(driver.get_screenshot_as_png(),
                      name='cart_screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        raise e


@allure.step("to add product to bag and verify cart details before checkout")
def add_to_bag_and_verify_cart_details(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(productlocators.product_instruction).send_keys(instructions)
    except:
        print("no instructions")
    try:
        try:
            By_xpath(productlocators.add_to_bag).click()
        except:
            By_xpath(productlocators.add_to_bag_btn2).click()
        time.sleep(2)
        print("added to bag")
        By_xpath(productlocators.cart_btn).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='cart_screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To verify increment of the item quantity and price details in cart")
def increase_item_in_cart(driver):
    By_xpath = driver.find_element_by_xpath
    try:

        By_xpath(cartLocators.cart_increment_btn).click()
        time.sleep(2)
        By_xpath(cartLocators.cart_increment_btn).click()
        time.sleep(2)
        print("item increased")

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("To verify decrement of the item quantity and price details in cart")
def decrease_item_in_cart(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        # get details before decrement the item quantity
        By_xpath(cartLocators.cart_decrement_btn).click()
        time.sleep(2)
        By_xpath(cartLocators.cart_decrement_btn).click()
        time.sleep(2)

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(
        ), name='Exception_screen', attachment_type=AttachmentType.PNG)
        raise e


@allure.step("edit items")
def edit_items(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(cartLocators.edit_btn).click()
        time.sleep(3)
        By_id(productlocators.product_instruction).clear()
        By_id(productlocators.product_instruction).send_keys(
            "Send Pickles and extra toppings")
        By_id(cartLocators.increase_qty).click()
        By_id(cartLocators.increase_qty).click()

    except Exception as ex:
        raise ex


@allure.step("empty cart")
def delete_items_empty_cart(driver):
    By_xpath = driver.find_element_by_xpath
    no_of_items = By_xpath(cartLocators.item_number).text
    no_of_items = no_of_items[0]
    print(no_of_items)
    no_of_items = int(no_of_items)
    try:
        while no_of_items > 0:
            By_xpath(cartLocators.delete_item).click()
            By_xpath(cartLocators.remove_btn).click()
            print("item deleted")
            try:
                heading = By_xpath(cartLocators.empty_cart_headng).text
                print(heading)
                assert heading == "YOUR BAS IS EMPTY."

            except:
                no_of_items = By_xpath(cartLocators.item_number).text
                no_of_items = no_of_items[0]
                print(no_of_items)
                no_of_items = int(no_of_items)
        try:
            tax = By_xpath(cartLocators.estimated_tax2).text
            time.sleep(1)
            assert tax in "$0.00"
        except:
            print("no delivery fee in pickup")
        time.sleep(1)
        checkout = By_xpath(cartLocators.checkout_price).text
        time.sleep(1)
        assert checkout in "$0.00"
    except Exception as ex:
        raise ex


@allure.step("Checkout")
def Checkout(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(cartLocators.checkout_btn).click()
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@allure.step("Checkout to payment screen")
def Checkout_to_paymentscreen(driver, email, password):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(cartLocators.checkout_btn).click()
        time.sleep(3)
        try:
            time.sleep(5)
            By_xpath(loginlocators.usename_xpath).send_keys(email)
            By_xpath(loginlocators.password_xpath).send_keys(password)
            By_xpath(loginlocators.signin_btn).click()
            time.sleep(2)
            signed_in = By_xpath(loginlocators.home_signin_btn).text
            print(signed_in)
            assert signed_in in "RITU"
            return signed_in
        except:
            print("Already sign in")

        cart_heading1 = By_xpath(paymentLocators.cart_summary_hedng).text
        time.sleep(2)
        assert cart_heading1 in "CART SUMMARY"
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@allure.step("To add a new Delivery Address at checkout stage.")
def add_new_del_add(driver, address):
    By_xpath = driver.find_element_by_xpath
    By_name = driver.find_element_by_name
    try:
        try:
            By_xpath(checkoutlocators.plus_add_address).click()
        except:
            By_xpath(checkoutlocators.plus_add_address2).click()
        By_name(loginlocators.new_add_field).send_keys(address)
        time.sleep(3)
        By_name(loginlocators.new_add_field).send_keys(Keys.DOWN)
        time.sleep(1)
        By_name(loginlocators.new_add_field).send_keys(Keys.ENTER)
        time.sleep(3)
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
        time.sleep(7)
        address_list = driver.find_elements_by_xpath(
            checkoutlocators.address_list)
        print(address)
        # for i in address_list:
        #     print(i.text)
        #     assert address in i.text
    except Exception as e:
        raise e


@allure.step("To remove a Delivery Address at checkout stage.")
def remove_del_add(driver, address):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        By_xpath(checkoutlocators.remove_add_btn).click()
        time.sleep(2)
        By_xpath(checkoutlocators.remove_ok_btn).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        raise e


@allure.step("To edit a existing Delivery Address at checkout stage.")
def edit_del_add(driver, hno):
    By_xpath = driver.find_element_by_xpath
    By_name = driver.find_element_by_name
    try:
        By_xpath(checkoutlocators.edit_add_btn).click()
        By_name(checkoutlocators.edit_hno_field).clear()
        By_name(checkoutlocators.edit_hno_field).send_keys(hno)
        time.sleep(1)
        By_xpath(checkoutlocators.save_this_address_btn).click()
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
        time.sleep(7)
        address_list = driver.find_elements_by_xpath(
            checkoutlocators.address_list)
        for i in address_list:
            print(i.text)
            assert hno in i.text
    except Exception as e:
        raise e


@allure.step("To add new card")
def add_new_card(driver, name, number, month, year, cvc):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        try:
            By_xpath(checkoutlocators.plus_card_details).click()
        except:
            By_xpath(checkoutlocators.plus_card_details2).click()
        time.sleep(2)
        By_xpath(checkoutlocators.card_owner_name).send_keys(name)
        By_xpath(checkoutlocators.new_card_number).send_keys(number)
        Select(By_xpath(checkoutlocators.new_expiry_month)
               ).select_by_visible_text(month)
        # Select(By_id(checkoutlocators.new_expiry_year)).select_by_visible_text(year)
        By_xpath(checkoutlocators.new_cvc).send_keys(cvc)
        By_xpath(checkoutlocators.billing_address).send_keys(
            "1322 Northern ways, US")
        time.sleep(2)
        By_xpath(checkoutlocators.billing_address).send_keys(Keys.DOWN)
        By_xpath(checkoutlocators.billing_address).send_keys(Keys.ENTER)
        time.sleep(1)
        By_xpath(checkoutlocators.save_card_btn).click()
        time.sleep(6)
        print(name)
        card_list = driver.find_elements_by_xpath(
            checkoutlocators.card_list)
        for i in card_list:
            print(i.text)
            assert name in i.text
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(
        ), name='card_screen_failure', attachment_type=AttachmentType.PNG)
        raise ex


@allure.step("To remove a saved card at checkout stage.")
def remove_saved_card(driver):
    By_xpath = driver.find_element_by_xpath
    By_id = driver.find_element_by_id
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        By_xpath(checkoutlocators.remove_card_btn).click()
        time.sleep(2)
        By_xpath(checkoutlocators.remove_card_ok).click()
        time.sleep(4)
        By_xpath(checkoutlocators.ok_success_btn).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        raise e


@ allure.step("palace your order")
def place_ur_order_from_payment(driver, status):
    By_xpath = driver.find_element_by_xpath
    try:
        time.sleep(3)
        cart_heading1 = By_xpath(paymentLocators.cart_summary_hedng).text
        time.sleep(2)
        assert cart_heading1 in "CART SUMMARY"
        time.sleep(2)
        if status == "Delivery":
            By_xpath(paymentLocators.select_delivery_address).click()
            time.sleep(2)
        else:
            print("Pickup order")
        By_xpath(paymentLocators.payment_card).click()
        time.sleep(2)
        By_xpath(paymentLocators.palce_ur_ordr).click()
        time.sleep(2)

        allure.attach(driver.get_screenshot_as_png(),
                      name='screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@allure.step("To delete a item from the cart")
def delete_from_cart(driver, item):
    By_xpath = driver.find_element_by_xpath
    By_xpath(productlocators.cart2).click()
    time.sleep(4)
    a = driver.find_element_by_xpath(productlocators.deleted_item)
    time.sleep(1)
    a.click()
    time.sleep(1)
    driver.find_element_by_xpath(productlocators.yes_btn).click()
    time.sleep(3)
    driver.refresh()
    cart = driver.find_element_by_xpath(productlocators.cart_table).text
    assert item not in cart
    print("Not added to bag")
    allure.attach(driver.get_screenshot_as_png(),
                  name='cart_screen', attachment_type=AttachmentType.PNG)


@ allure.step("To be able to empty all the bag")
def empty_cart(driver):
    By_xpath = driver.find_element_by_xpath
    By_xpath(productlocators.cart2).click()
    time.sleep(4)
    time.sleep(2)
    try:
        driver.find_element_by_xpath(productlocators.empty_bag2).click()
        time.sleep(2)
    except:
        driver.find_element_by_xpath(productlocators.empty_bag).click()
        time.sleep(2)
    try:
        driver.find_element_by_xpath(productlocators.empty_cart_yes).click()
    except:
        driver.find_element_by_xpath(productlocators.empty_cart_yes2).click()
    time.sleep(3)
    # driver.refresh()

    try:
        cart = driver.find_element_by_xpath(
            productlocators.empty_bag_heading).text
        assert "0 Items" in cart
    except:
        home_page = By_xpath(checkoutlocators.home_page_heading).text
        print(home_page)
        assert home_page == "Experience the Best Food at Best In Town"

    allure.attach(driver.get_screenshot_as_png(),
                  name='cart_screen', attachment_type=AttachmentType.PNG)


@ allure.step("To change order setting to Pickup option")
def order_setting(driver, order_type):
    By_xpath = driver.find_element_by_xpath
    try:
        if order_type == "Pickup":
            By_xpath(checkoutlocators.pickup_path).click()
        else:
            By_xpath(checkoutlocators.delivery_path).click()
        time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(
        ), name='order_setting_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To verify order details after order placement")
def verify_order_details(driver, order_type, timeslot):
    By_xpath = driver.find_element_by_xpath
    try:
        order_status = By_xpath(placedPaymentLocators.order_status).text
        order_number = By_xpath(placedPaymentLocators.order_number).text
        assert order_type in order_status
        print("order_type matched")
        allure.attach(driver.get_screenshot_as_png(
        ), name='final_order_setting_screen', attachment_type=AttachmentType.PNG)
        return order_number
    except Exception as e:
        raise e


@ allure.step("To change order setting to Delivery option")
def asap_setting(driver, address):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.del_link_path).click()
        time.sleep(2)
        Select(By_xpath(productlocators.address_field)).select_by_value(address)
        allure.attach(driver.get_screenshot_as_png(
        ), name='asap_order_setting_screen', attachment_type=AttachmentType.PNG)
        time.sleep(3)
        By_xpath(productlocators.change_date_time_path).click()
        time.sleep(2)
        By_xpath(loginlocators.asap_btn).click()
        time.sleep(2)
        By_xpath(loginlocators.now_btn).click()
        time.sleep(2)
        # order_label=By_xpath(productlocators.order_label).text
        # print(order_label)
        # assert "ASAP" in order_label

    except Exception as e:
        raise e


@ allure.step("Later order setting to Delivery option")
def later_order_setting(driver, date, timeslot, address):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(productlocators.del_link_path).click()
        time.sleep(2)
        Select(By_xpath(productlocators.address_field)).select_by_value(address)
        allure.attach(driver.get_screenshot_as_png(
        ), name='later_order_setting_screen', attachment_type=AttachmentType.PNG)
        time.sleep(3)
        By_xpath(productlocators.change_date_time_path).click()
        time.sleep(2)
        By_xpath(loginlocators.later_btn).click()
        time.sleep(2)
        # find_element_by_text(driver, date).click()
        time.sleep(2)
        Select(By_xpath(loginlocators.later_time)).select_by_value(timeslot)
        time.sleep(2)
        By_xpath(productlocators.final_btn).click()
        time.sleep(2)
        By_xpath(productlocators.update_btn).click()
        time.sleep(2)
        try:
            err = By_xpath(productlocators.invalid_address_err).text
            print(err)
            assert err == "Please set valid address for delivery"
        except:
            print("not error")
            # driver.refresh()
            time.sleep(5)
            # order_label=By_xpath(productlocators.order_label).text
            # print(order_label)
            # assert order_type in order_label
            # assert timeslot in order_label
            allure.attach(driver.get_screenshot_as_png(
            ), name='final_order_setting_screen', attachment_type=AttachmentType.PNG)

    except Exception as e:
        raise e


@allure.step("To proceed with checkout")
def checkout(driver):
    By_xpath = driver.find_element_by_xpath
    # By_xpath=driver.find_element_by_xpath
    By_xpath(productlocators.cart2).click()
    time.sleep(4)
    By_xpath(productlocators.checkout_btn).click()
    try:
        checkout_button = find_element_by_text(driver, "Place your order!")
        assert True
    except:
        assert False
    time.sleep(4)


@ allure.step("To order details confirmation")
def pickup_order_confirm_info(driver, customername, pickuptime):
    By_xpath = driver.find_element_by_xpath
    try:
        # name=By_xpath(checkoutlocators.contact_name).text
        # assert customername in name
        heading = By_xpath(checkoutlocators.order_setting_heading).text
        assert "PICKUP ADDRESS" in heading
        detail = By_xpath(checkoutlocators.cust_detail).text
        assert customername in detail
        assert "Pickup" in detail
        # order_time =By_xpath(checkoutlocators.date_time).text
        # print(order_time)
        print(pickuptime)
        assert pickuptime in detail

        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To order details confirmation")
def delivery_order_confirm_info(driver, customername, date_time):
    By_xpath = driver.find_element_by_xpath
    try:
        # name=By_xpath(checkoutlocators.contact_name).text
        # assert customername in name
        # order_time =By_xpath(checkoutlocators.date_time).text
        # assert order_time in date_time
        heading = By_xpath(checkoutlocators.order_setting_heading).text
        assert "DELIVERY ADDRESS" in heading
        detail = By_xpath(checkoutlocators.cust_detail).text
        assert customername in detail
        assert "Delivery" in detail
        # order_time =By_xpath(checkoutlocators.date_time2).text
        assert date_time in detail
        # By_xpath(checkoutlocators.delivery_instructions).click()
        # By_xpath(checkoutlocators.inst_textarea).send_keys("Double Cheese")
        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To order details confirmation")
def asap_confirm_info(driver, customername, date_time):
    By_xpath = driver.find_element_by_xpath
    try:
        # name=By_xpath(checkoutlocators.contact_name).text
        # assert customername in name
        # order_time =By_xpath(checkoutlocators.date_time).text
        # assert order_time in date_time
        heading = By_xpath(checkoutlocators.order_setting_heading).text
        assert "DELIVERY ADDRESS" in heading
        detail = By_xpath(checkoutlocators.cust_detail).text
        assert customername in detail
        assert "ASAP" in detail

        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("to change order setting at payment page")
def change_setting_to_delivery(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.change_settings).click()
        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
        time.sleep(2)
    except Exception as e:
        raise e


@ allure.step("to change order setting at payment page")
def change_setting_to_pickup(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.change_settings).click()
        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To add a customise tip from customer")
def custom_tip(driver, tip):
    By_xpath = driver.find_element_by_xpath
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        By_xpath(checkoutlocators.custome_tip_btn).click()
        time.sleep(2)
        By_xpath(checkoutlocators.tip_xpath).clear()
        time.sleep(5)
        By_xpath(checkoutlocators.tip_xpath).send_keys("3")
        time.sleep(6)
        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)
    except Exception as e:
        raise e


@ allure.step("To add tip according to percentage")
def fix_tip(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.percent_tip).click()
    except Exception as ex:
        raise ex


@ allure.step("To proceed to payments")
def checkout2(driver):
    try:
        find_element_by_text(driver, "Place your order!").click()
        allure.attach(driver.get_screenshot_as_png(
        ), name='Review_place order_screen', attachment_type=AttachmentType.PNG)
        try:
            Select(driver.find_element_by_xpath(checkoutlocators.secnd_deli_field)
                   ).select_by_visible_text("4600 Roosevelt Boulevard, Philadelphia, PA, USA")
            find_element_by_text(driver, "Update").click()
        except:
            print("2nd")
    except Exception as ex:
        raise ex
    time.sleep(3)


@ allure.step("To enter wrong delivery address")
def wrong_address(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # By_xpath(checkoutlocators.contact_address).clear()
        By_xpath(checkoutlocators.contact_address).send_keys(
            "456,Housing Board Colony,Rajasthan,India")
        # By_xpath(checkoutlocators.contact_spec_ins).send_keys("No Extra Cheese Please")
        allure.attach(driver.get_screenshot_as_png(
        ), name='confirminfo_screen', attachment_type=AttachmentType.PNG)

        find_element_by_text(driver, "Continue to payment method").click()
        time.sleep(3)
        err_msg = By_xpath(checkoutlocators.invalid_add_err_msg).text
        assert err_msg == "Please set valid address for delivery"
    except Exception as e:
        raise e


@ allure.step(" To verify order details on payment screen")
def review_details(driver, name, order_type):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.change_card_btn).click()
        time.sleep(2)
        order = By_xpath(checkoutlocators.order_type).text
        print(order)
        name_in = By_xpath(checkoutlocators.name_in_order).text
        print(name)
        assert name == name_in
        assert order == order_type
    except Exception as ex:
        raise ex


@ allure.step("To verify successful payment by selecting one of thesaved card. ")
def select_card(driver, selected_card):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.change_card_btn).click()
        time.sleep(2)
        Select(By_xpath(checkoutlocators.select_card)
               ).select_by_visible_text(selected_card)
        allure.attach(driver.get_screenshot_as_png(),
                      name='pament_screen', attachment_type=AttachmentType.PNG)
        By_xpath(checkoutlocators.place_order_btn).click()
        time.sleep(3)
        Thank_heading = By_xpath(checkoutlocators.Thank_heading).text
        allure.attach(driver.get_screenshot_as_png(
        ), name='order_placed_screen', attachment_type=AttachmentType.PNG)
        assert Thank_heading == "THANK YOU!"
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(
        ), name='card_screen_failure', attachment_type=AttachmentType.PNG)
        raise ex


@ allure.step("To verify successful payment by selecting one of thesaved card. ")
def delete_card(driver, selected_card):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.change_card_btn).click()
        time.sleep(2)
        Select(By_xpath(checkoutlocators.select_card)
               ).select_by_visible_text(selected_card)
        allure.attach(driver.get_screenshot_as_png(),
                      name='pament_screen', attachment_type=AttachmentType.PNG)
        By_xpath(checkoutlocators.delete_card).click()
        time.sleep(1)
        try:
            Select(By_xpath(checkoutlocators.select_card)
                   ).select_by_visible_text(selected_card)
            assert False
        except:
            assert True
    except Exception as ex:
        allure.attach(driver.get_screenshot_as_png(
        ), name='card_screen_failure', attachment_type=AttachmentType.PNG)
        raise ex


@ allure.step("To make credit card payments")
def credit_card_payment(driver, name, number, month, year, cvc, remember):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(checkoutlocators.card_name).send_keys(name)
        time.sleep(7)
        By_xpath(checkoutlocators.card_number).send_keys(number)
        By_xpath(checkoutlocators.month).send_keys(month)
        By_xpath(checkoutlocators.year).send_keys(year)
        By_xpath(checkoutlocators.cvc).send_keys(cvc)
        if remember == "Yes":
            By_xpath(checkoutlocators.remember_card).click()
            time.sleep(2)
        allure.attach(driver.get_screenshot_as_png(),
                      name='pament_screen', attachment_type=AttachmentType.PNG)
        By_xpath(checkoutlocators.place_order_btn).click()
        time.sleep(3)
        Thank_heading = By_xpath(checkoutlocators.Thank_heading).text
        print(Thank_heading)
        assert Thank_heading == "THANK YOU!"
    except Exception as e:
        raise e


@ allure.step("final order confirmation screen")
def get_order_number(driver):
    try:
        order_number = driver.find_element_by_xpath(
            checkoutlocators.order_num_p).text
        print(order_number)
        order = order_number.split()
        print(order[2])
        order_no = order[2]
        allure.attach(driver.get_screenshot_as_png(
        ), name='Thank_you_screen', attachment_type=AttachmentType.PNG)
        find_element_by_text(driver, "Continue to homepage").click()
        time.sleep(3)
        return order_no
    except Exception as e:
        raise e


@ allure.step("To verify get home page using profile link click")
def get_homepage_using_profile_link(driver):
    By_xpath = driver.find_element_by_xpath
    try:
        By_xpath(loginlocators.signedin_label).click()
        time.sleep(4)
        By_xpath(loginlocators.profile_btn).click()
        time.sleep(8)
        heading1 = By_xpath(loginlocators.home_page_heading).text
        time.sleep(2)
        print(heading1)
        assert heading1 in "Experience the Best Food at Best In Town Pizzas"
    except Exception as e:
        raise e


@ allure.step("To verify get contact us info")
def get_contactus_info(driver):
    By_xpath = driver.find_element_by_xpath
    try:

        By_xpath(loginlocators.contact_us).click()
        time.sleep(2)
        heading1 = By_xpath(loginlocators.aboutus_heading).text
        print(heading1)
        assert heading1 in "ABOUT NEW STAR PIZZA"
        heading = By_xpath(loginlocators.openhours_heading).text
        assert heading in "BUSINESS HOURS"
        open_days = By_xpath(loginlocators.opendays).text
        assert open_days in "Monday - Thursday"
        open_hrs = By_xpath(loginlocators.openhours).text
        assert open_hrs in "11:00AM - 10:00PM"
        closeday = By_xpath(loginlocators.close_days).text
        assert closeday in "Friday & Saturday"
        close = By_xpath(loginlocators.close_text).text
        assert close in "11:00AM - 11:00PM"
        partial_day = By_xpath(loginlocators.partialday).text
        assert partial_day in "Sunday"
        sun_time = By_xpath(loginlocators.partial_time).text
        assert sun_time in "12:00PM - 10:00PM"
        time.sleep(2)
        By_xpath(loginlocators.arrow).click()
        time.sleep(2)
        top_headings = By_xpath(loginlocators.top_heading).text
        assert top_headings in "NEW STAR PIZZA"
    except Exception as e:
        raise e
