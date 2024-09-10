from playwright.sync_api import Page

class TestCasesPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_test_cases_page(self):
        assert self.page.url == 'https://www.automationexercise.com/test_cases'