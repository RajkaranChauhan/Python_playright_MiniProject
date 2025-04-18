import time

from playwright.sync_api import Page, expect

from all.utils import constant
from all.utils.all_action import AllAction
from all.utils.constant import Constant


class payment_method_page():

    def __init__(self, page:Page):
        self.page = page
        print(self.page)
        print("in payment method const")

    @property
    def payment_method_header(self):
        return self.page.get_by_text("Payment Method")

    @property
    def populated_email(self):
        return self.page.locator("//*[@class='user__name mt-5']//label")

    @property
    def txt_update_email(self):
        return self.page.locator("//*[@class='user__name mt-5']/input")

    @property
    def txt_box_country(self):
        return self.page.locator("//*[@placeholder='Select Country']")

    @property
    def value_country(self):
        return self.page.locator("//*[text()=' India']")

    @property
    def btn_place_order(self):
        return self.page.locator("//*[@class='btnn action__submit ng-star-inserted']")

    @property
    def header_order_confirmation(self):
        return self.page.locator("//*[text()=' Thankyou for the order. ']")

    @property
    def id_order_confirmation (self):
        return self.page.locator("//*[@class='em-spacer-1']//label[@class='ng-star-inserted']")

    @property
    def order_history_page_link(self):
        return self.page.locator("//*[@class='em-spacer-1']/*[@routerlink='/dashboard/myorders']")

    def in_my_payment_method_page(self):
        expect(self.payment_method_header).to_be_visible()
        print("user in Payment Method page")

    def verify_email(self, expected_email):
        actual_email = self.populated_email.text_content()
        print("actual_email :"+actual_email+" and expected_email : "+expected_email)
        assert actual_email == expected_email
        print("After compare actual_email :" + actual_email + " and expected_email : " + expected_email)

    def update_email(self, email):
        # time.sleep(5)
        self.txt_update_email.clear()
        # time.sleep(5)
        self.txt_update_email.fill(email)
        # time.sleep(5)

    def select_country(self, country):
        self.txt_box_country.click()
        self.txt_box_country.fill(country)
        self.page.keyboard.press("Backspace")#this need explaination
        self.value_country.click()
        print("Country selected as : "+country)

    def btn_place_order_clicked(self):
        self.btn_place_order.click()

    def get_confirmation_order_id(self):
        print("confirmation order id is : "+self.id_order_confirmation.text_content())
        # print(self.order_history_page_link.text_content())
        all_action=AllAction(self.page)
        all_action.verify_order_history_page_link(self.order_history_page_link)
        order_id= all_action.fetch_order_id(self.id_order_confirmation)
        constant.ORDER_ID =order_id
        print("Order id using constant class: "+ constant.ORDER_ID)


