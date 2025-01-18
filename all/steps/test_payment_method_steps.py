import os

import pytest
from pytest_bdd import scenarios, given, then, when, parsers

from .Pages.payment_method_page import payment_method_page

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
final_dir = os.path.join(parent_dir, 'features', 'd_payment_method.feature')
# final_dir1 =  os.path.join(parent_dir, 'features', 'a_login.feature')
scenarios(final_dir)


# Fixture to initialize LoginPage for reuse
@pytest.fixture
def payment_method(browser_instance):
    # global page
    # return LoginPage(browser_instance)
    return payment_method_page(browser_instance)


@given('User is in payment method page')
def step_given_user_on_payment_page(payment_method):
    payment_method.in_my_payment_method_page()


@then(parsers.parse('Verify the populated email is {email}'))
def step_then_verify_populated_email(payment_method, email):
    payment_method.verify_email(email)


@then(parsers.parse('User update the email to {new_email}'))
def step_then_update_email(payment_method, new_email):
    payment_method.update_email(new_email)




@then(parsers.parse('User selects the country as {country}'))
def step_then_select_country(payment_method, country):
    payment_method.select_country(country)


@when('User click on the button Place Order')
def step_when_click_place_orders(payment_method):
    payment_method.btn_place_order_clicked()


@then('User should be in Order confirmation page')
def step_then_verify_order_confirmation_page(payment_method):
    payment_method.get_confirmation_order_id()
