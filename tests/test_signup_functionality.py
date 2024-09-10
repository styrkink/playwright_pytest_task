import pytest
import allure
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.random_data_generator import RandomUser
from data.test_data import email2


class TestSignup:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_page = SignupPage(self.page)

        self.home_page.verify_home_page()
        self.home_page.accept_cookies()
        self.home_page.click_signup_btn()
        self.signup_page.verify_signup_header_visible()

    @pytest.mark.three
    @allure.step("Sign up and delete account")
    def test_signup_and_delete_account(self, test_setup):
        with allure.step("Fill in the sign-up form"):
            self.signup_page.fill_signup_form(
                RandomUser.generate_name(),
                RandomUser.generate_email()
            )
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Signup Form Filled",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Submit sign-up form"):
            self.signup_page.sumbit_signup_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Signup Form Submitted",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify account form header is visible"):
            self.signup_page.verify_account_form_header_visible()

        with allure.step("Fill in account details form"):
            self.signup_page.fill_signup_details_form(
                RandomUser.generate_password(),
                RandomUser.generate_first_name(),
                RandomUser.generate_last_name(),
                RandomUser.generate_company_name(),
                RandomUser.generate_address(),
                RandomUser.generate_address_details(),
                RandomUser.generate_state(),
                RandomUser.generate_city(),
                RandomUser.generate_zipcode(),
                RandomUser.generate_phone_number()
            )
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Details Filled",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Create account"):
            self.signup_page.click_create_account_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Created",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify account created"):
            self.signup_page.verify_account_created()

        with allure.step("Continue to home page"):
            self.signup_page.click_continue_btn()
            self.home_page.verify_login()

        with allure.step("Delete account"):
            self.home_page.click_delete_account_btn()
            self.home_page.verify_account_deleted()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Deleted",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Continue after account deletion"):
            self.signup_page.click_continue_btn()

    @pytest.mark.three
    @allure.step("Sign up with existing email")
    def test_signup_with_exist_email(self, test_setup):
        random_name = RandomUser.generate_name()
        exist_email = email2

        with allure.step("Fill in the sign-up form with existing email"):
            self.signup_page.fill_signup_form(random_name, exist_email)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Signup Form with Existing Email",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Submit sign-up form"):
            self.signup_page.sumbit_signup_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'),
                          name="Signup Form Submitted with Existing Email", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify error message is visible"):
            self.signup_page.verify_signup_error_message_visible()
