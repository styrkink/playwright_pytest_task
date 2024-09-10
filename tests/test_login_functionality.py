import pytest
import allure

from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.random_data_generator import RandomUser
from data.test_data import email1, password


class TestLogin:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.signup_page = SignupPage(self.page)
        self.valid_email = email1
        self.valid_password = password
        self.random_email = RandomUser.generate_email()
        self.random_password = RandomUser.generate_password()

        self.home_page.accept_cookies()
        self.home_page.verify_home_page()
        self.home_page.click_signup_btn()

    @pytest.mark.two
    @allure.step("Attempt login with invalid credentials")
    def test_invalid_credentials_login(self, test_setup):
        with allure.step("Fill login form with invalid credentials"):
            self.signup_page.fill_login_form(self.random_email, self.random_password)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Invalid Login Form Filled",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Submit login form"):
            self.signup_page.submit_login_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Login Form Submitted",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify error message for invalid login"):
            self.signup_page.verify_login_error_message_visible()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Login Error Message Visible",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.two
    @allure.step("Perform logout")
    def test_logout(self, test_setup):
        with allure.step("Fill login form with valid credentials"):
            self.signup_page.fill_login_form(self.valid_email, self.valid_password)
            self.signup_page.submit_login_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Login Form Filled for Logout",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify login"):
            self.home_page.verify_login()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Login Verified for Logout",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Click logout button"):
            self.home_page.click_logout_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Logout Button Clicked",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify signup page is displayed after logout"):
            self.signup_page.verify_signup_page()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Signup Page Verified After Logout",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.two
    @allure.step("Perform valid login")
    def test_valid_login(self, test_setup):
        with allure.step("Fill login form with valid credentials"):
            self.signup_page.fill_login_form(self.valid_email, self.valid_password)
            self.signup_page.submit_login_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Login Form Filled",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify login"):
            self.home_page.verify_login()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Login Verified",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Delete account"):
            self.home_page.click_delete_account_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Delete Account Button Clicked",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify account deletion"):
            self.home_page.verify_account_deleted()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Account Deleted",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Continue after account deletion"):
            self.signup_page.click_continue_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Continue Button Clicked",
                          attachment_type=allure.attachment_type.PNG)
