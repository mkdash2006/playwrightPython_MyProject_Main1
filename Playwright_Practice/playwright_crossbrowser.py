# Cross Browser Testing - Chromium, Firefox, Webkit

from playwright.sync_api import sync_playwright
import time

def browserLaunch(engine="chromium"):
    with sync_playwright() as p:
        if engine == "chromium":
            browser = p.chromium.launch(headless=False)
            print("Launched: Chromium (Chrome/Edge)")
        elif engine == "firefox":
            browser = p.firefox.launch(headless=False)
            print("Launched: Firefox")
        elif engine == "webkit":
            browser = p.webkit.launch(headless=False)
            print("Launched: WebKit (Safari)")
        else:
            raise ValueError("Unknown engine")

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
        print (f"Browser window is opened with {tab_count1} tabs")

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
        time.sleep(5)
        tab_count2 = len(context2.pages)
        print (f"2nd Browser window is opened with {tab_count2} tabs")
        #print(f"Page title in {engine}: {page1.title()}")
        browser.close()

browserLaunch("chromium")
#browserLaunch("firefox")
#browserLaunch("webkit")