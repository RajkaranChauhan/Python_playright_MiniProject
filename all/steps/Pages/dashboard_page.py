import time

from playwright.sync_api import Page, expect


class dashboard_page:
    def __init__(self, page: Page):
        self.page = page
        print("in dashboard const")

    @property
    def home_page_dashboard(self):
        return self.page.get_by_text("Automation Practice")

    @property
    def cart(self):
        return self.page.locator("//*[@class='btn btn-custom']//*[@class='fa fa-shopping-cart']")

    @property
    def btn_home(self):
        return self.page.locator("//*[@class='fa fa-home']")


    def in_dashboard_home_page(self):
        self.btn_home.click()
        expect(self.home_page_dashboard).to_be_visible()
        print("user in dashboard home page")

    def goto_cart(self):
        self.cart.click()
        time.sleep(1)

    def add_shoe(self, prod):
        product = self.page.locator("//*[@class='card']").filter(has_text=prod)
        product.get_by_text("Add To Cart").click()

    # def navigate_to_application(self):
    #     self.page.goto("https://rahulshettyacademy.com/client")
    #     print("user in application")



