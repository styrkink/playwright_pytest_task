import pytest
import allure

from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage

class TestTestCases:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.test_cases_page = TestCasesPage(self.page)

    @pytest.mark.seven
    @allure.step("Open test cases page")
    def test_open_test_cases_page(self, test_setup):

        with allure.step("Verify home page and accept cookies"):
            self.home_page.verify_home_page()
            self.home_page.accept_cookies()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Home Page Verified", attachment_type=allure.attachment_type.PNG)

        with allure.step("Click on test cases button"):
            self.home_page.click_test_cases_btn()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Test Cases Button Clicked", attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify test cases page"):
            self.test_cases_page.verify_test_cases_page()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Test Cases Page Verified", attachment_type=allure.attachment_type.PNG)
