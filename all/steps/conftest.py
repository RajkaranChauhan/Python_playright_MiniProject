import pytest
from playwright.sync_api import Playwright

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser selection: chrome or firefox"
    )

# if used as session then the same browser will be used till end
# used as function then for each scenario the browser will be created like congnito no data stored

@pytest.fixture(scope="session")
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name").lower()
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page  # Provide the page to the test
    context.close()
    browser.close()

'''
function (default):

A new instance of the fixture is created for every test function that uses it.
This scope is useful when you need a fresh setup for each test to ensure isolation between tests.

class:
A single instance of the fixture is created for each test class, and it will be shared across all the test methods within that class.
This is useful when the setup is expensive, but you still want to avoid recreating it for each individual test method.

module:
A single instance of the fixture is created for each test module. It will be shared across all the test functions in that module.
Ideal for cases where the setup is expensive but can be reused across multiple test functions within the same module.

package:
A single instance of the fixture is created for each package, meaning that it will be shared across all the test modules within the same package.
Use this scope when you want to share a setup across multiple modules in the same package.

session:
A single instance of the fixture is created for the entire test session. It will be shared across all test modules, functions, and classes in the session.
This is the most global scope and is typically used for fixtures that set up a testing environment that lasts for the entire test run, such as a database connection or web server.
'''
