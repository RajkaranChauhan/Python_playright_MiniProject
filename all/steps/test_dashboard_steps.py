import os
import time

import pytest
from pytest_bdd import scenarios, given, then, parsers

from .Pages.dashboard_page import dashboard_page
from .Pages.login_page import login_page

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))
final_dir = os.path.join(parent_dir, 'features', 'b_dashboard.feature')
# final_dir1 =  os.path.join(parent_dir, 'features', 'a_login.feature')
scenarios(final_dir)


# Fixture to initialize LoginPage for reuse
@pytest.fixture
def paged(browser_instance):
    # global page
    # return LoginPage(browser_instance)
    return dashboard_page(browser_instance)


@pytest.fixture
def login(browser_instance):
    return login_page(browser_instance)


@given(parsers.parse("User login to the application using {user} and {passw} as credentials and is in dashboard page"))
def user_login_in_app(login, user, passw):
    login.navigate_to_application()
    login.enter_user(user)
    login.enter_pass(passw)
    login.btn_login_clicked()
    login.app_login_success()


@given("user should navigate to the Dashboard page")
def dashboard_page_displayed(paged):
    paged.in_dashboard_home_page()
    print("Dashboard steps")
    time.sleep(1)


@then(parsers.parse("add {product}"))
def shoe_added(paged, product):
    paged.add_shoe(product)
    print("product added : " + product)


# @then(parsers.parse("add {phone}"))
# def phone_added(paged,phone):
#     print("Dashboard steps" +phone)

@then("go to Cart")
def goto_cart(paged):
    paged.goto_cart()
    print("User navigated to cart")
    time.sleep(1)



