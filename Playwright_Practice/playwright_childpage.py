from playwright.sync_api import sync_playwright, expect

def Test_childpage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/", timeout=6000)

        with page.expect_popup() as cp:
            page.locator("[onclick='myFunction()']").click()
        page2 = cp.value
        print(page2.title())

Test_childpage()