from playwright.sync_api import sync_playwright, expect
#import time

def Test_pageassert():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.wait_for_timeout(2000)
        # Python Assert 
        #assert page.title() == "Automation Testing Practice123" 
        #playwright Assert    
        #expect(page).to_have_title("Automtoation Testing Practice123", timeout=5000) 
        expect(page.locator("#name")).to_be_visible(timeout=5000)
        expect(page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]")).to_have_text("Learn Selenium")
        expect(page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]")).to_contain_text("Learn Selenium")

Test_pageassert()



