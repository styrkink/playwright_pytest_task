import pytest
from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.__signup_btn = self.page.locator('//a[text()=" Signup / Login"]')
        self.__contact_btn = self.page.locator('a[href="/contact_us"]')
        self.__accept_cookies_btn = self.page.locator('button[aria-label="Consent"]')
        self.__logged_user_message = self.page.locator('//a[text()=" Logged in as "]')
        self.__delete_account_btn = self.page.locator('a[href="/delete_account"]')
        self.__account_deleted_message = self.page.locator('h2:has-text("Account Deleted!")')
        self.__logout_btn = self.page.locator('a[href="/logout"]')
        self.__test_cases_btn = self.page.locator('//a[text()=" Test Cases"]')
        self.__cart_btn = self.page.locator('//a[text()=" Cart"]')
        self.__products_btn = self.page.locator('//a[text()=" Products"]')

    def verify_home_page(self):
        assert self.page.title() == "Automation Exercise"

    def click_signup_btn(self):
        self.__signup_btn.click(force=True)

    def accept_cookies(self):
        try:
            if self.__accept_cookies_btn.is_visible():
                self.__accept_cookies_btn.click()
        except TimeoutError:
            pytest.skip("Cookies acceptance button not found, skipping related steps.")


    def verify_login(self):
        assert self.__logged_user_message.is_visible()

    def click_delete_account_btn(self):
        self.__delete_account_btn.click()

    def verify_account_deleted(self):
        assert self.__account_deleted_message.is_visible()

    def click_logout_btn(self):
        self.__logout_btn.click()

    def click_contact_btn(self):
        self.__contact_btn.click(force=True)

    def click_test_cases_btn(self):
        self.__test_cases_btn.click(timeout=60000)

    def click_cart_btn(self):
        self.__cart_btn.click()

    def click_products_btn(self):
        self.__products_btn.click()








