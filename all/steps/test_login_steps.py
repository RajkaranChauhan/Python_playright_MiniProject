import os

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from .Pages.login_page import login_page

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)
parent_dir =  os.path.abspath(os.path.join(script_dir, ".."))
print("parent"+parent_dir)
final_dir = os.path.join(parent_dir, 'features', 'a_login.feature')
print("final_dir "+final_dir)
# features_dir = os.path.join(script_dir, 'features', 'llogin.feature')
# print(features_dir)
# boo = os.path.exists(features_dir)
# print("path exists: " + str(boo))

# scenarios("features/llogin.feature")
scenarios(final_dir)

# Fixture to initialize LoginPage for reuse
@pytest.fixture
def login(browser_instance):
    return login_page(browser_instance)


@given("the login page is displayed")
def display_login_page(login):
    # login.navigate_to_application()
    login.navigate_to_application()


@when(parsers.parse('I enter {email} in the email field'))
def enter_email(login, email):
    login.enter_user(email)


@when(parsers.parse("I enter {password} in the password field"))
def enter_password(login, password):
    login.enter_pass(password)


@when("I click on the login button")
def click_login_button(login):
    login.btn_login_clicked()


@then("I should be logged into the application")
def application_logged_in(login):
    login.app_login_success()
