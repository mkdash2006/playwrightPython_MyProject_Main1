from playwright.sync_api import sync_playwright
import time

def browserLaunch():
    # p = sync_playwright().start()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)     # Launch Chrome browser
        #browser = p.firefox.launch(headless=False)     # Launch Firefox browser
        #browser = p.webkit.launch(headless=False)      # Launch Webkit/Safari browser

        # Launch multiple tabs in Browser window
        context1 = browser.new_context() # 2. New/1st Browser/session/context/window
        page1 = context1.new_page() # 1st Tab
        page2 = context1.new_page() # 2nd Tab
        page3 = context1.new_page() # 3rd Tab
        page1.goto("https://testautomationpractice.blogspot.com/")
        page2.goto("https://testautomationpractice.blogspot.com/")
        page3.goto("https://testautomationpractice.blogspot.com/")
        time.sleep(3)
        tab_count1 = len(context1.pages)
        #tab_count2 = len(context2.pages)
        print (f"Browser window is launched with {tab_count1} tabs")

        # Launch multiple tabs in 2nd window
        context2 = browser.new_context() # 2. New Browser/session/context/window
        page4 = context2.new_page() # 1st Tab
        page5 = context2.new_page() # 2nd Tab
        page6 = context2.new_page() # 3rd Tab
        page7 = context2.new_page() # 4th Tab
        page4.goto("https://testautomationpractice.blogspot.com/")
        page5.goto("https://testautomationpractice.blogspot.com/")
        page6.goto("https://testautomationpractice.blogspot.com/")
        page7.goto("https://testautomationpractice.blogspot.com/")
        time.sleep(1)
        tab_count2 = len(context2.pages)
        print (f"2nd Browser window is launched with {tab_count2} tabs")
        browser.close()
        return tab_count1, tab_count2

        # title = [page1.title(), page2.title(), page3.title()]
        # return title
        # p.stop()
browserLaunch("chromium")