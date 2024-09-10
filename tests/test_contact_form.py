import pytest
import allure

from pages.home_page import HomePage
from pages.contact_page import ContactPage
from utils.random_data_generator import RandomUser, RandomMessage
from data.test_data import file_path

class TestContactForm:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.contact_page = ContactPage(self.page)

        self.random_name = RandomUser.generate_name()
        self.random_email = RandomUser.generate_email()
        self.random_subject = RandomMessage.generate_subject()
        self.random_message = RandomMessage.generate_message()
        self.file_path = file_path

    @pytest.mark.six
    @allure.step("Submit valid contact form")
    def test_valid_contact_form(self, test_setup):


        with allure.step("Verify home page and accept cookies"):
            self.home_page.verify_home_page()
            self.home_page.accept_cookies()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Home Page Verified", attachment_type=allure.attachment_type.PNG)

        with allure.step("Click on contact button"):
            self.home_page.click_contact_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Contact Button Clicked", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify contact form header"):
            self.contact_page.verify_contact_form_header()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Contact Form Header Verified", attachment_type=allure.attachment_type.PNG)

        with allure.step("Fill in the contact form"):
            self.contact_page.fill_contact_from(self.random_name, self.random_email, self.random_subject, self.random_message)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Contact Form Filled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Upload a file to the contact form"):
            self.contact_page.upload_contact_file(self.file_path)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="File Uploaded", attachment_type=allure.attachment_type.PNG)

        with allure.step("Handle dialog and submit the contact form"):
            self.page.once("dialog", lambda dialog: dialog.accept())
            self.contact_page.submit_contact_from()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Contact Form Submitted", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify success message is visible"):
            self.contact_page.verify_success_message_visible()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Success Message Verified", attachment_type=allure.attachment_type.PNG)

        with allure.step("Click home button and verify home page"):
            self.contact_page.click_home_btn()
            self.home_page.verify_home_page()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Home Page Verified After Submission", attachment_type=allure.attachment_type.PNG)
