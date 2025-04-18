import time

from playwright.sync_api import expect
from playwright.sync_api import Page


class my_cart():
    def __init__(self, page:Page):
        self.page = page
        print(self.page)
        print("in my cart const")

    @property
    def my_cart_header(self):
        return self.page.locator("//*[text()='My Cart']")

    @property
    def btn_checkout(self):
        return self.page.get_by_role("button",name="Checkout")

    @property
    def payment_method_header(self):
        return self.page.get_by_text("Payment Method")

    @property
    def items_in_cart(self):
        return self.page.locator("//*[@class='cartSection']/..")

    def in_my_cart_page(self):
        expect(self.my_cart_header).to_be_visible()
        print("user in My Cart page")

    def in_my_payment_method_page(self):
        expect(self.payment_method_header).to_be_visible()
        print("user in Payment Method page")

    def clicked_checkout_button(self):
        self.btn_checkout.click()
        print("Checkout button clicked")

    def remove_product(self, prod):
        product = self.items_in_cart.filter(has_text=prod)
        product.locator("//*[@class='btn btn-danger']").click()
        print("product removed from cart is : "+ prod)
        time.sleep(1)
