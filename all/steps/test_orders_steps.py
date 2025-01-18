import os

import pytest
from playwright.sync_api import Page
from pytest_bdd import scenarios, when, then, parsers

from all.steps.Pages.orders_page import orders_page

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
final_dir = os.path.join(parent_dir, 'features', 'e_orders.feature')
# final_dir1 =  os.path.join(parent_dir, 'features', 'a_login.feature')
scenarios(final_dir)


# Shared fixture for the orders page
@pytest.fixture
def orders(browser_instance):
    return orders_page(browser_instance)

# Step definitions
@when("User clicks on the Orders button user navigates to order details page")
def step_navigate_to_orders_page(orders):
    orders.click_btn_orders()

@then("Verify the Order is available there")
def step_verify_order_available(orders):
    orders.verify_order_id()

@when("User clicks on the View button of the order id that he made he moves to order summary page")
def step_click_view_button(orders):
    orders.click_btn_view()

@then("Verify order id is displayed there")
def step_verify_order_id_displayed(orders):
    orders.order_id_order_summary_pages()

@then(parsers.parse("Verify Delivery Address has email as {email}"))
def step_verify_delivery_address_email(orders,  email):
    orders.email_verify(email)