import pytest
import allure
from pages.home_page import HomePage
from pages.footer_page import FooterPage
from utils.random_data_generator import RandomUser

class TestSubscribe:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.footer_page = FooterPage(self.page)

        self.random_email = RandomUser.generate_email()

        self.home_page.verify_home_page()
        self.home_page.accept_cookies()

    @pytest.mark.four
    @allure.step("Subscribe from home page")
    def test_home_page_subscription(self, test_setup):
        with allure.step("Scroll to footer"):
            self.footer_page.scroll_to_footer()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Footer Scrolled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify subscribe header is visible"):
            self.footer_page.verify_subscribe_header_visible()

        with allure.step("Fill subscribe email"):
            self.footer_page.fill_subscribe_email(self.random_email)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Email Filled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Submit subscribe form"):
            self.footer_page.submit_subscribe_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Form Submitted", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify subscribe header is still visible"):
            self.footer_page.verify_subscribe_header_visible()

    @pytest.mark.four
    @allure.step("Subscribe from cart page")
    def test_cart_page_subscription(self, test_setup):
        with allure.step("Click cart button"):
            self.home_page.click_cart_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Cart Button Clicked", attachment_type=allure.attachment_type.PNG)

        with allure.step("Scroll to footer"):
            self.footer_page.scroll_to_footer()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Footer Scrolled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify subscribe header is visible"):
            self.footer_page.verify_subscribe_header_visible()

        with allure.step("Fill subscribe email"):
            self.footer_page.fill_subscribe_email(self.random_email)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Email Filled", attachment_type=allure.attachment_type.PNG)

        with allure.step("Submit subscribe form"):
            self.footer_page.submit_subscribe_form()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Form Submitted", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify subscribe header is still visible"):
            self.footer_page.verify_subscribe_header_visible()
