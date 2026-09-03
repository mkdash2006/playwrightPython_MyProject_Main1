# Playwright Instsllstion - 
# Step 1- Install Playwright, to get all Methods. Prompt is ->
#         pip install plywright  (generally used in all machines, ex-windows) OR
#         python -m pip install playwright (in some machine if not recognized.)
#         python -m playwright install - push/forcefully install playwright package
#         python3 -m playwright install - for mac machine
# Step 2- To install Browser (Playwright have its own browser enginee ex-chromium, Firefox, Webkit/Safari)
#         playwright instsall
# Step 3- To check in CMD or Terminal
#         playwright --version  OR  pip list OR playwright -m OR  python3 --version



# from playwright.sync_api import sync_playwright

"""with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    print(page.title())
    browser.close() """
############################### Open in same Browser, different Tab, Reliable one is Context
"""with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page1 = browser.new_page()
    page2 = browser.new_page()
    page1.goto("https://testautomationpractice.blogspot.com/")
    page2.goto("https://www.amazon.in/")
    print(page1.title())
    print(page2.title())
    page1.wait_for_timeout(8000)
    page2.wait_for_timeout(8000)
    browser.close() """
############################### Open in same Browser, different Tab using Context
"""with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page1 = context.new_page()
    page2 = context.new_page()
    page1.goto("https://testautomationpractice.blogspot.com/")
    page2.goto("https://ishatrainingsolutions.org/")
    # Wait until DOM is ready before reading titles
    #page1.wait_for_load_state("domcontentloaded")
    #page2.wait_for_load_state("domcontentloaded")
    #page2.wait_for_selector("h1")   # wait until the main heading is visible
    # Wait until the title contains expected text
    page2.wait_for_function("document.title.includes('Isha Training Solutions')")
    print(page1.title())
    print(page2.title())
    #page1.wait_for_timeout(5000)
    #page2.wait_for_timeout(5000)
    #page2.wait_for_load_state("domcontentloaded")   # wait until DOM is ready
    browser.close()
    
from PlaywrightMethods import browserLaunch
browserLaunch() 
"""
##############################################################################
