from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.__products_list = self.page.locator('[class="features_items"]')
        self.__product_details_name = self.page.locator('.product-information h2')
        self.__product_details_category = self.page.locator('.product-information p:has-text("Category")')
        self.__product_details_price = self.page.locator('.product-information span span')
        self.__product_details_availability = self.page.locator('.product-information p b:has-text("Availability:")')
        self.__product_details_condition = self.page.locator('.product-information p b:has-text("Condition:")')
        self.__product_details_brand = self.page.locator('.product-information p:has-text("Brand:")')
        self.__product_search_input = self.page.locator('#search_product')
        self.__submit_search_btn = self.page.locator('#submit_search')
        self.__searched_products_header = self.page.locator('h2:has-text("Searched Products")')
        self.__product_name = self.page.locator('[class="productinfo text-center"] p')
        self.__continue_shopping_btn = self.page.locator('button:has-text("Continue Shopping")')
        self.__quantity_input = self.page.locator('#quantity')
        self.__add_to_cart_btn = self.page.locator('button:has-text("Add to cart")')
        self.__view_cart_btn = self.page.locator('#cartModal > div > div > div.modal-body > p:nth-child(2) > a > u')

    def verify_products_page(self):
        assert self.page.url == 'https://www.automationexercise.com/products'

    def verify_products_list_visible(self):
        assert self.__products_list.is_visible()

    def click_view_product_btn(self, product_id: str):
        self.page.locator(f'a[href="/product_details/{product_id}"]').click()

    def verify_product_details_page(self, product_id: str):
        current_url = self.page.url
        expected_url = f'https://www.automationexercise.com/product_details/{product_id}'
        assert current_url == expected_url, f"Expected URL {expected_url} but got {current_url}"

    def verify_product_details_visible(self):
        assert self.__product_details_name.is_visible()
        assert self.__product_details_category.is_visible()
        assert self.__product_details_price.is_visible()
        assert self.__product_details_availability.is_visible()
        assert self.__product_details_condition.is_visible()
        assert self.__product_details_brand.is_visible()

    def search_and_verify_products(self, search_word: str):
        self.__product_search_input.fill(search_word)
        self.__submit_search_btn.click()
        self.page.wait_for_selector('[class="features_items"]')
        assert self.__searched_products_header.is_visible()

        product_count = self.__product_name.count()
        for i in range(product_count):
            product_name = self.__product_name.nth(i).inner_text().lower()
            assert search_word.lower() in product_name

    def click_continue_shopping_btn(self):
        self.__continue_shopping_btn.click()

    def click_view_cart_btn(self):
        self.page.locator('a:has-text("View Cart")').wait_for(state='visible', timeout=10000)
        self.page.locator('a:has-text("View Cart")').click(force=True)

    def add_product_to_cart(self, product_id: str):
        self.page.locator(f'div.productinfo a[data-product-id="{product_id}"]').hover()
        self.page.locator(f'div.overlay-content a[data-product-id="{product_id}"]').wait_for(state="visible", timeout=10000)
        self.page.locator(f'div.overlay-content a[data-product-id="{product_id}"]').click()

    def set_product_quantity(self, quantity: str):
        self.__quantity_input.fill(quantity)

    def click_add_to_cart(self):
        self.__add_to_cart_btn.click()



