import pytest
import allure
import random

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.signup_page import SignupPage
from utils.random_data_generator import RandomUser, RandomMessage, RandomCardDetails

class TestCheckout:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = ProductsPage(self.page)
        self.cart_page = CartPage(self.page)
        self.signup_page = SignupPage(self.page)
        self.generate_random_user_data()
        self.home_page.verify_home_page()
        self.home_page.accept_cookies()

    def generate_random_user_data(self):
        self.name = RandomUser.generate_name()
        self.email = RandomUser.generate_email()
        self.password = RandomUser.generate_password()
        self.first_name = RandomUser.generate_first_name()
        self.last_name = RandomUser.generate_last_name()
        self.company_name = RandomUser.generate_company_name()
        self.address1 = RandomUser.generate_address()
        self.address2 = RandomUser.generate_address_details()
        self.state = RandomUser.generate_state()
        self.city = RandomUser.generate_city()
        self.zipcode = RandomUser.generate_zipcode()
        self.phone_number = RandomUser.generate_phone_number()
        self.random_message = RandomMessage.generate_message()
        self.card_number = RandomCardDetails.generate_card_number()
        self.cvc = RandomCardDetails.generate_cvc()
        self.expiry_month = str(random.randint(1, 12))
        self.expiry_year = str(random.randint(2024, 2055))

    def register_user(self):
        with allure.step("Fill and submit the signup form"):
            self.signup_page.fill_signup_form(self.name, self.email)
            self.signup_page.sumbit_signup_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Signup Form Submitted", attachment_type=allure.attachment_type.PNG)

        with allure.step("Fill and submit additional signup details"):
            self.signup_page.verify_account_form_header_visible()
            self.signup_page.fill_signup_details_form(
                self.password, self.first_name, self.last_name, self.company_name,
                self.address1, self.address2, self.state, self.city, self.zipcode, self.phone_number
            )
            self.signup_page.click_create_account_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Details Submitted", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify account creation and login"):
            self.signup_page.verify_account_created()
            self.signup_page.click_continue_btn()
            self.home_page.verify_login()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Created and Logged In", attachment_type=allure.attachment_type.PNG)

    def add_products_to_cart(self):
        with allure.step("Add products to cart"):
            self.products_page.add_product_to_cart("1")
            self.products_page.click_continue_shopping_btn()
            self.products_page.add_product_to_cart("2")
            self.home_page.click_cart_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Products Added to Cart", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify cart page"):
            self.cart_page.verify_cart_page()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Cart Page Verified", attachment_type=allure.attachment_type.PNG)

    def checkout_order(self):
        with allure.step("Verify order details and fill in comment"):
            self.cart_page.verify_order_details(self.address1, self.address2, self.phone_number)
            self.cart_page.fill_comment_input(self.random_message)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Order Details Verified", attachment_type=allure.attachment_type.PNG)

        with allure.step("Place the order and provide payment details"):
            self.cart_page.click_place_order_btn()
            self.cart_page.fill_pay_details(self.first_name, self.last_name, self.card_number,
                                            self.cvc, self.expiry_month, self.expiry_year)
            self.cart_page.click_confirm_pay_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Payment Details Submitted", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify order placed message"):
            self.cart_page.verify_order_placed_message_visible()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Order Placed", attachment_type=allure.attachment_type.PNG)

    def delete_account(self):
        with allure.step("Delete account and verify deletion"):
            self.home_page.click_delete_account_btn()
            self.home_page.verify_account_deleted()
            self.signup_page.click_continue_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Deleted", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.one
    @allure.step("Register while checking out")
    def test_register_while_checkout(self, test_setup):
        with allure.step("Navigate to products page and add products to cart"):
            self.home_page.click_products_btn()
            self.products_page.verify_products_page()
            self.products_page.verify_products_list_visible()
            self.add_products_to_cart()

        with allure.step("Proceed to checkout and register"):
            self.cart_page.click_checkout_btn()
            self.cart_page.click_register_login_btn()
            self.register_user()
            self.home_page.click_cart_btn()
            self.cart_page.click_checkout_btn()
            self.checkout_order()
            self.delete_account()

    @pytest.mark.one
    @allure.step("Register before checking out")
    def test_register_before_checkout(self, test_setup):
        with allure.step("Navigate to signup page and register"):
            self.home_page.click_signup_btn()
            self.signup_page.verify_signup_header_visible()
            self.register_user()

        with allure.step("Navigate to products page and add products to cart"):
            self.home_page.click_products_btn()
            self.products_page.verify_products_page()
            self.products_page.verify_products_list_visible()
            self.add_products_to_cart()

        with allure.step("Proceed to checkout"):
            self.cart_page.click_checkout_btn()
            self.checkout_order()
            self.delete_account()
