
from playwright.sync_api import Page, sync_playwright
import pytest

@pytest.fixture()
def navigateToAmazan(page: Page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(3000)
    # countOfBtns = page.locator("")   # If any interim pages will come before opening homepage. eb- timeout page, 
    # if countOfBtns > 0:
    #     page.locator("").click()


# @pytest.fixture(autouse=True)     
# def precondition():
#     print("TC Precondition")
#     yield
#     print("TC Postcondition")

##############################  Not required, if pytest default fixtures installed (pip install pytest-playwright)
# @pytest.fixture(autouse=True)
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         yield browser

# @pytest.fixture(autouse=True)
# def context():
#     with sync_playwright() as p:
#         browser = p.chromium.launch()
#         context = browser.new_context()
#         yield context

# @pytest.fixture(autouse=True)
# def page():
#     with sync_playwright() as p:
#         browser= p.chromium.launch()
#         context= browser.new_context()
#         page= context.new_page()
#         yield page
############################################