from faker.generator import random
from playwright.sync_api import Page
import random

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.__signup_header = self.page.locator('h2:has-text("New User Signup!")')
        self.__login_header = self.page.locator('h2:has-text("Login to your account")')
        self.__name_input = self.page.locator('input[name="name"]')
        self.__email_input = self.page.locator('input[data-qa="signup-email"]')
        self.__submit_btn = self.page.locator('//button[text()="Signup"]')
        self.__account_form_header = self.page.locator('h2:has-text("Enter Account Information")')
        self.__password_input = self.page.locator('#password')
        self.__day_dropdown = self.page.locator('#days')
        self.__month_dropdown = self.page.locator('#months')
        self.__year_dropdown = self.page.locator('#years')
        self.__newsletter_checkbox = self.page.locator('#newsletter')
        self.__optin_checkbox = self.page.locator('#optin')
        self.__first_name_input = self.page.locator('#first_name')
        self.__last_name_input = self.page.locator('#last_name')
        self.__company_name_input = self.page.locator('#company')
        self.__address_input = self.page.locator('#address1')
        self.__address_details_input = self.page.locator('#address2')
        self.__country_dropdown = self.page.locator('#country')
        self.__state_input = self.page.locator('#state')
        self.__city_input = self.page.locator('#city')
        self.__zipcode_input = self.page.locator('#zipcode')
        self.__phone_number_input = self.page.locator('#mobile_number')
        self.__create_account_btn = self.page.locator('//button[text()="Create Account"]')
        self.__account_created_message = self.page.locator('h2:has-text("Account Created!")')
        self.__continue_btn = self.page.locator('a[data-qa="continue-button"]')
        self.__login_email_input = self.page.locator('input[data-qa="login-email"]')
        self.__login_password_input = self.page.locator('input[data-qa="login-password"]')
        self.__login_btn = self.page.locator('button[data-qa="login-button"]')
        self.__login_error_message = self.page.locator('p[style="color: red;"]:has-text("Your email or password is incorrect!")')
        self.__signup_error_message = self.page.locator('p[style="color: red;"]:has-text("Email Address already exist!")')

    def verify_signup_header_visible(self):
        assert self.__signup_header.is_visible()

    def fill_signup_form(self, name: str, email: str):
        self.__name_input.fill(name)
        self.__email_input.fill(email)

    def sumbit_signup_form(self):
        self.__submit_btn.click()

    def verify_login_header_visible(self):
        assert self.__login_header.is_visible()

    def verify_account_form_header_visible(self):
        assert self.__account_form_header.is_visible()

    def fill_signup_details_form(self, password: str, first_name: str, last_name: str,
                                 company_name: str, address: str, address_details: str,
                                 state: str, city: str, zipcode: str, phone_number: str):
        genders = ['gender1', 'gender2']
        random_gender = random.choice(genders)
        radio_button = self.page.locator(f'input[id="id_{random_gender}"]')
        radio_button.check()
        self.__password_input.fill(password)
        random_day = str(random.randint(1, 31))
        random_month = str(random.randint(1, 12))
        random_year = str(random.randint(1900, 2021))
        self.__day_dropdown.select_option(random_day)
        self.__month_dropdown.select_option(random_month)
        self.__year_dropdown.select_option(random_year)
        self.__newsletter_checkbox.check()
        self.__optin_checkbox.check()
        self.__first_name_input.fill(first_name)
        self.__last_name_input.fill(last_name)
        self.__company_name_input.fill(company_name)
        self.__address_input.fill(address)
        self.__address_details_input.fill(address_details)
        options = self.__country_dropdown.locator("option").all_text_contents()
        random_option = random.choice(options)
        self.__country_dropdown.select_option(label=random_option)
        self.__state_input.fill(state)
        self.__city_input.fill(city)
        self.__zipcode_input.fill(zipcode)
        self.__phone_number_input.fill(phone_number)

    def click_create_account_btn(self):
        self.__create_account_btn.click()

    def verify_account_created(self):
        assert self.__account_created_message.is_visible()

    def click_continue_btn(self):
        self.__continue_btn.click()

    def fill_login_form(self, email: str, password: str):
        self.__login_email_input.fill(email)
        self.__login_password_input.fill(password)

    def submit_login_form(self):
        self.__login_btn.click(force=True)

    def verify_login_error_message_visible(self):
        assert self.__login_error_message.is_visible()

    def verify_signup_page(self):
        assert self.page.url == 'https://www.automationexercise.com/login'

    def verify_signup_error_message_visible(self):
        assert self.__signup_error_message.is_visible()








