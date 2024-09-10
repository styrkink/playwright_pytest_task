from playwright.sync_api import Page
import pytest

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.__contact_form_header = self.page.locator('//h2[text()="Get In Touch"]')
        self.__contact_name_input = self.page.locator('input[data-qa="name"]')
        self.__contact_email_input = self.page.locator('input[data-qa="email"]')
        self.__contact_subject_input = self.page.locator('input[data-qa="subject"]')
        self.__contact_message_input = self.page.locator('#message')
        self.__upload_file_input = self.page.locator('input[name="upload_file"]')
        self.__submit_contact_form_btn = self.page.locator('input[data-qa="submit-button"]')
        self.__success_message = self.page.locator('div.status.alert.alert-success')
        self.__home_btn = self.page.locator('a.btn.btn-success[href="/"]')

    def verify_contact_form_header(self) -> None:
        assert self.__contact_form_header.is_visible()

    def fill_contact_from(self, name: str, email: str, subject: str, message: str):
        self.__contact_name_input.fill(name)
        self.__contact_email_input.fill(email)
        self.__contact_subject_input.fill(subject)
        self.__contact_message_input.fill(message)

    def upload_contact_file(self, file_path: str):
        with self.page.expect_file_chooser() as file_chooser_info:
            self.__upload_file_input.click()
        file_chooser = file_chooser_info.value
        file_chooser.set_files(file_path)

    def submit_contact_from(self):
        self.__submit_contact_form_btn.click()

    def verify_success_message_visible(self):
        self.page.wait_for_selector("div.status.alert.alert-success", state="visible")
        assert self.__success_message.is_visible()

    def click_home_btn(self):
        self.__home_btn.click()




