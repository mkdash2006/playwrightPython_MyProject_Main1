# Alerts - Simple Alert (one option- 'OK' in popup)- dialog.accept()
# Confirmation Alert (Two option- OK and Cancel in popup) - dialog.dismiss()
# Prompt Alert (Three option - Text field to enter, OK and Cancel) - dialog.message

from playwright.sync_api import sync_playwright, expect

# def Test_handle_alerts():
#     with sync_playwright() as p:
#         browser= p.chromium.launch(headless=False)
#         context= browser.new_context()
#         page= context.new_page()
#         page.goto("https://testautomationpractice.blogspot.com/", timeout=60000)

#         # Handle Alerts
#         # Accept
#         def handlealert1(dialog1):
#             page.wait_for_timeout(3000)
#             dialog1.accept()
#         page.once("dialog", handlealert1)        # Execute always within the test case
#         #page.once("dialog", handlealert1)     # Execute ony once within the test case
#         page.locator("button#alertBtn").click()
#         page.wait_for_timeout(3000)

#         # Dismiss
#         def handlealert2(dialog2):
#             page.wait_for_timeout(3000)
#             dialog2.dismiss()
#         page.once("dialog", handlealert2)
#         page.locator("button#confirmBtn").click()
#         expect(page.locator("p#demo")).to_have_text("You pressed Cancel!")
#         page.wait_for_timeout(3000)

#         # # Accept with Message
#         def handlealert3(dialog3):
#             page.wait_for_timeout(3000)
#             #print(dialog3.message)
#             dialog3.accept("Manoj")
#         page.once("dialog", handlealert3)
#         page.locator("button#promptBtn").click()
#         expect(page.locator("p#demo")).to_have_text("Hello Manoj! How are you today?")
#         page.wait_for_timeout(6000)
        
# Test_handle_alerts()
############################
# Lambda- It uses only once, replace for one liner function
# def m1(a)
#     print(a)
# m1 = lambda a: print(a)
############################
def Test_handle_alerts_lamda():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        context= browser.new_context()
        page= context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/", timeout=60000)
        
        # Function with Lamda
        page.on("dialog", lambda dialog: dialog.dismiss())
        page.wait_for_timeout(6000)

        page.locator("button#confirmBtn").click()
        page.wait_for_timeout(6000)

Test_handle_alerts_lamda()

