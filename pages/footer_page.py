from playwright.sync_api import Page

class FooterPage:
    def __init__(self, page: Page):
        self.page = page
        self.__subscribe_header = self.page.locator('h2:has-text("Subscription")')
        self.__subscribe_email = self.page.locator('#susbscribe_email')
        self.__submit_subscribe_btn = self.page.locator('#subscribe')
        self.__success_subscribe_message = self.page.locator('#success-subscribe')

    def verify_subscribe_header_visible(self):
        assert self.__subscribe_header.is_visible()

    def scroll_to_footer(self):
        self.__subscribe_header.scroll_into_view_if_needed()

    def fill_subscribe_email(self, email: str):
        self.__subscribe_email.fill(email)

    def submit_subscribe_form(self):
        self.__submit_subscribe_btn.click()

    def verify_success_subscribe(self):
        assert self.__success_subscribe_message.is_visible()