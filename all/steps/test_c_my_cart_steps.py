import os

import pytest
from pytest_bdd import scenarios, given, then, when, parsers

from .Pages.c_my_cart_page import my_cart

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
final_dir = os.path.join(parent_dir, 'features', 'c_my_cart.feature')
# final_dir1 =  os.path.join(parent_dir, 'features', 'a_login.feature')
scenarios(final_dir)


# Fixture to initialize LoginPage for reuse
@pytest.fixture
def cart(browser_instance):
    # global page
    # return LoginPage(browser_instance)
    return my_cart(browser_instance)


@given("User is in my cart page")
def step_user_in_cart_page(cart):
    cart.in_my_cart_page()


@then(parsers.parse("Remove the product {product} from cart"))
def step_remove_product_from_cart(cart,product):
    cart.remove_product(product)


@when("User clicks on the checkout button")
def step_click_checkout_button(cart):
    cart.clicked_checkout_button()


@then("User moves to the payment Method page")
def step_user_moves_to_payment_page(cart):
    cart.in_my_payment_method_page()

