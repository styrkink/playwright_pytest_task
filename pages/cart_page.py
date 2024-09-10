from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.__checkout_button = self.page.locator('a.btn.check_out')
        self.__register_login_btn = self.page.locator('a:has-text("Register / Login")')
        self.__comment_input = self.page.locator('textarea.form-control[name="message"]')
        self.__place_order_btn = self.page.locator('a.btn.btn-default.check_out[href="/payment"]')
        self.__card_holder_name_input = self.page.locator('input[data-qa="name-on-card"]')
        self.__card_number_input = self.page.locator('input[data-qa="card-number"]')
        self.__card_cvc_input = self.page.locator('input[data-qa="cvc"]')
        self.__card_expiry_month_input = self.page.locator('input[data-qa="expiry-month"]')
        self.__card_expiry_year_input = self.page.locator('input[data-qa="expiry-year"]')
        self.__confirm_pay_btn = self.page.locator('#submit')
        self.__order_placed_message = self.page.locator('h2[data-qa="order-placed"]')

    def verify_products_in_cart(self, product_ids: list):
        for product_id in product_ids:
            product_in_cart = self.page.locator(f'#product-{product_id}')
            assert product_in_cart.is_visible(), f"Product with ID {product_id} not found in cart"

    def verify_product_quantity(self, quantity: str):
        quantity_locator = self.page.locator(f'button:has-text("{quantity}")')
        quantity_locator.wait_for(state='visible', timeout=10000)
        actual_quantity = quantity_locator.inner_text().strip()
        assert actual_quantity == quantity, f"Expected quantity '{quantity}', but got '{actual_quantity}'"

    def verify_cart_page(self):
        assert self.page.url == 'https://www.automationexercise.com/view_cart'

    def click_checkout_btn(self):
        self.__checkout_button.click()

    def click_register_login_btn(self):
        self.__register_login_btn.click()

    def verify_order_details(self, address1, address2, phone):
        address1_locator = self.page.locator('#address_delivery > li').nth(3)
        address2_locator = self.page.locator('#address_delivery > li').nth(4)
        phone_locator = self.page.locator('#address_delivery > li').nth(7)

        actual_address1 = address1_locator.inner_text().replace("\n", " ").strip()
        actual_address2 = address2_locator.inner_text().replace("\n", " ").strip()
        actual_phone = phone_locator.inner_text().strip()

        expected_address1 = address1.replace("\n", " ").strip()
        expected_address2 = address2.replace("\n", " ").strip()

        assert actual_address1 == expected_address1, f"Expected address1 to be {expected_address1}, but got {actual_address1}"
        assert actual_address2 == expected_address2, f"Expected address2 to be {expected_address2}, but got {actual_address2}"
        assert actual_phone == phone, f"Expected phone to be {phone}, but got {actual_phone}"

    def fill_comment_input(self, random_message: str):
        self.__comment_input.fill(random_message)

    def click_place_order_btn(self):
        self.__place_order_btn.click()

    def fill_pay_details(self,
                         first_name: str,
                         last_name: str,
                         card_number: str,
                         cvc: str,
                         expiry_month: str,
                         expiry_year: str):
        self.__card_holder_name_input.fill(f"{first_name} {last_name}")
        self.__card_number_input.fill(card_number)
        self.__card_cvc_input.fill(cvc)
        self.__card_expiry_month_input.fill(expiry_month)
        self.__card_expiry_year_input.fill(expiry_year)

    def click_confirm_pay_btn(self):
        self.__confirm_pay_btn.click()

    def verify_order_placed_message_visible(self):
        self.__order_placed_message.wait_for(state='visible', timeout=5000)
        assert self.__order_placed_message.is_visible(), f"Success payment message is not visible"

