from playwright.sync_api import sync_playwright
"""
def browserLaunch():
    # p = sync_playwright().start()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # Launch Chrome browser
        # Launch multiple tabs in Chrome window
        context = browser.new_context() # 2. New/1st Browser/session/context/window
        page01=context.new_page() # 1st Tab
        page02=context.new_page() # 2nd Tab
        page03=context.new_page() # 3rd Tab
        page01.goto("https://testautomationpractice.blogspot.com/")
        page02.goto("https://testautomationpractice.blogspot.com/")
        page03.goto("https://testautomationpractice.blogspot.com/")
        page01.wait_for_timeout(1000)
        page02.wait_for_timeout(1000)
        page03.wait_for_timeout(1000)
        b1tab_count = len(context.pages)
        print (f"1st Chrome Browser window is launched with {b1tab_count} tabs")

        # Launch multiple tabs in 2nd window
        context1 = browser.new_context() # 2. New Browser/session/context/window
        page1=context1.new_page() # 1st Tab
        page2=context1.new_page() # 2nd Tab
        page3=context1.new_page() # 3rd Tab
        page4=context1.new_page() # 4th Tab
        page1.goto("https://testautomationpractice.blogspot.com/")
        page2.goto("https://testautomationpractice.blogspot.com/")
        page3.goto("https://testautomationpractice.blogspot.com/")
        page4.goto("https://testautomationpractice.blogspot.com/")
        page1.wait_for_timeout(1000)
        page2.wait_for_timeout(1000)
        page3.wait_for_timeout(1000)
        page4.wait_for_timeout(1000)
        b2tab_count = len(context1.pages)
        print (f"2nd Chrome Browser window is launched with {b2tab_count} tabs")
        # title = [page1.title(), page2.title(), page3.title()]
        # return title
        # p.stop()

        browser.close()
        return b1tab_count, b2tab_count
      
browserLaunch()
###########################################################
"""
"""
def browsenavigation():
    with sync_playwright() as p: 
        # 'with' statement to ensure auto start & stop of all resources.
        browser = p.chromium.launch(headless=False) # Browser type
        context = browser.new_context() # New browser Session
        page = context.new_page()     # New page Opened
        page.goto("https://testautomationpractice.blogspot.com/")     # Goto URL
        page.wait_for_timeout(3000)
        page.go_back()
        page.wait_for_timeout(3000)
        page.go_forward()
        page.wait_for_timeout(3000)
        page.reload()
        page.wait_for_timeout(3000)
        print("Page Title is:", page.title())
        page.wait_for_timeout(3000)
        print("URL is:", page.url)
        page.wait_for_timeout(3000)
        
browsenavigation()
"""
################################################################

