from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.smoke4

def test_login(page:Page, navigateToAmazan):       # page:Page (playwright fixture :playwright Datatype)
    page.get_by_text("Hello, Sign in").click()
    page.locator("span#nav-link-accountList-nav-line-1").click()
    page.wait_for_timeout(3000)
    page.locator("input#ap_email_login").fill("mk@gmail.com")
    page.wait_for_timeout(3000)
    page.locator("span#continue").click()
    page.wait_for_timeout(3000)
    page.locator("input#ap_password").fill("password2")
    page.wait_for_timeout(3000)
    page.locator("span#auth-signin-button").click()
    page.wait_for_timeout(2000)
    expect(page.get_by_text("Your password is incorrect"))

      
    
