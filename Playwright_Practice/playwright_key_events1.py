from playwright.sync_api import sync_playwright

def mouse_keyboard_event():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        # Keyboard Event
        page.locator("input#name").fill("Manoj")
        page.wait_for_timeout(4000)
        page.keyboard.press("Control+A")
        page.keyboard.press("Control+C")
        page.keyboard.press("Tab")
        page.keyboard.press("Control+V")
        page.wait_for_timeout(2000)
        # Hover
        page.locator("button.dropbtn").hover()
        page.wait_for_timeout(2000)
        page.locator("button.dropbtn").scroll_into_view_if_needed()
        # Right Click
        page.locator("//button[@ondblclick='myFunction1()']").click(button="right")
        page.keyboard.press("Escape")
        page.wait_for_timeout(1000)
    
        # Double Click
        #page.locator("//button[@ondblclick='myFunction1()']").dblclick()
        #page.locator("//button[@ondblclick='myFunction1()']").click(click_count=2)
        page.locator("//button[@ondblclick='myFunction1()']").scroll_into_view_if_needed()
        #print copied value
        print("Field2 Copied Value:", page.locator("input#field2").input_value())
        page.locator("input#field2").scroll_into_view_if_needed()
        page.wait_for_timeout(4000)
        # Drag & Drop
        #page.locator("div#draggable").drag_to.page.locator("div#droppable")

mouse_keyboard_event()