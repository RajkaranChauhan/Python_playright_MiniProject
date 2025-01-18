from playwright.sync_api import Page, Locator

import os


class AllAction():
    def __init__(self, page: Page):
        self.page = page

    def verify_order_history_page_link(self, element: Locator):
        print(element.text_content())
        print("verify_order_history_page_link")

    def fetch_order_id(self, element: Locator):
        odr_id = element.text_content()
        print("need to fetch order id for: "+odr_id)
        order_id=odr_id.strip(" | ")
        print("actual order id from allAction class : "+order_id)
        return order_id




