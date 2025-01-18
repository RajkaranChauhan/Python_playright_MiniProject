from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import page

from all.utils import constant


class orders_page():

    def __init__(self, page: Page):
        self.page = page
        print("in orders page const")

    @property
    def btn_order(self):
        return self.page.get_by_role("button", name="ORDERS")

    @property
    def header_order_page(self):
        return self.page.locator(".ng-star-inserted h1")

    @property
    def all_order_row_values(self):
        return self.page.locator("table.table-bordered tbody")

    @property
    def order_id_row(self):
        return self.page.locator("//*[@scope='row']")

    def product_order_id(self, id):
        self.id = id
        return self.page.locator(f"//*[text()='{self.id}']")

    # ("//*[text()='" + self.id + "']")  not to be used

    def btn_view(self, id):
        self.id = id
        return self.page.locator(f"//*[text()='{self.id}']/..//*[@class='btn btn-primary']")

    @property
    def header_order_summary_page(self):
        return self.page.locator(".email-preheader .tagline")

    @property
    def order_id_order_summary_page(self):
        return self.page.locator(".email-container .col-text.-main")

    @property
    def email_id_order_summary_page(self):
        return self.page.locator("(//*[@class='address']//*[@class='text'])[1]")

    def click_btn_orders(self):
        self.btn_order.click()
        print("ORDERS button clicked")
        txt = self.header_order_page.text_content()
        print("page header of orders page is : " + txt)

    def verify_order_id(self):
        id = constant.ORDER_ID
        print(id)

        order_locator = self.product_order_id(id)
        if order_locator.count() > 0:
            print(f"Order found: {order_locator.text_content()}")
        else:
            print("the Order id did not found in order summary page. Order id: " + id)
            assert False

    def click_btn_view(self):
        id = constant.ORDER_ID
        # if (self.all_order_row_values.filter(has_text=order_id).count() > 0):
        product_locator = self.btn_view(id)
        if product_locator.count() > 0:
            product_locator.click()
            print(f"VIEW button clicked for product id :{id}")

        else:
            print("VIEW button for  Order id : " + id + " was not found")
            assert False

    def order_id_order_summary_pages(self):
        txt = self.order_id_order_summary_page.text_content()
        order_id = constant.ORDER_ID
        assert txt == order_id
        print("ORDER SUMMARY page, order id displayed as : " + txt)

    def email_verify(self, email):
        self.email = email
        mail = self.email_id_order_summary_page.text_content().strip()
        print(f"email: {self.email}")
        print(f"mail: {mail}")
        assert mail == email
        print("ORDER SUMMARY page, email id displayed as : " + mail)
