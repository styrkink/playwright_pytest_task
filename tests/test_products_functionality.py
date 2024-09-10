import pytest
import allure
import random

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.random_data_generator import RandomProductName

class TestProducts:

    @pytest.fixture
    def test_setup(self, new_page):
        self.page = new_page
        self.home_page = HomePage(self.page)
        self.products_page = ProductsPage(self.page)
        self.cart_page = CartPage(self.page)

        self.home_page.verify_home_page()
        self.home_page.accept_cookies()
        self.home_page.click_products_btn()
        self.products_page.verify_products_page()
        self.products_page.verify_products_list_visible()

    @pytest.mark.five
    @allure.step("Verify product list and details")
    def test_product_list_and_details(self, test_setup):
        with allure.step("Click view product button"):
            self.products_page.click_view_product_btn("1")
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Product Details Page",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Verify product details page"):
            self.products_page.verify_product_details_page("1")

        with allure.step("Verify product details visible"):
            self.products_page.verify_product_details_visible()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Product Details Visible",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.five
    @allure.step("Search products")
    def test_product_search(self, test_setup):
        search_word = RandomProductName.generate_search_word()

        with allure.step(f"Search for products with word: {search_word}"):
            self.products_page.search_and_verify_products(search_word)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Search Results",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.five
    @allure.step("Add products to cart")
    def test_add_products_in_cart(self, test_setup):
        product_ids = ["1", "2"]

        with allure.step("Add first product to cart"):
            self.products_page.add_product_to_cart("1")
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="First Product Added",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Continue shopping"):
            self.products_page.click_continue_shopping_btn()

        with allure.step("Add second product to cart"):
            self.products_page.add_product_to_cart("2")
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Second Product Added",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("View cart and verify products"):
            self.products_page.click_view_cart_btn()
            self.cart_page.verify_products_in_cart(product_ids)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Products in Cart",
                          attachment_type=allure.attachment_type.PNG)

    @pytest.mark.five
    @allure.step("Check product quantity in cart")
    def test_product_quantity_in_cart(self, test_setup):
        random_product_id = str(random.randint(1, 8))

        with allure.step(f"View product with ID: {random_product_id}"):
            self.products_page.click_view_product_btn(random_product_id)
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Product Details Page",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step(f"Set product quantity to 4"):
            self.products_page.verify_product_details_page(random_product_id)
            self.products_page.set_product_quantity("4")
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Quantity Set",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Add product to cart"):
            self.products_page.click_add_to_cart()
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Product Added to Cart",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("View cart and verify product quantity"):
            self.products_page.click_view_cart_btn()
            self.cart_page.verify_product_quantity("4")
            allure.attach(self.page.screenshot(full_page=True, type='png'), name="Product Quantity Verified",
                          attachment_type=allure.attachment_type.PNG)
