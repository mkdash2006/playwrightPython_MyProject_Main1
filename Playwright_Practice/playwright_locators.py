# Locator - - get by Locator (page.get_by_text(""), _placeholder. _alttext, _label, _role)
#           - Reletive xpath    - page.locator("//tagname[@id=value1]")
#                               - page.locator("//tagname[@class=valu2]")
#           - CSS    (page.locator("tagname#valu1"))

from playwright.sync_api import sync_playwright
#import time
def BrowserElements():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.get_by_text("Data Entry Form").wait_for(state='visible' timeout=45000)
        print(page.title(), "-> Data Entry Form")
        
        page.get_by_placeholder("Enter Name").fill("Peter")
        page.get_by_placeholder("Enter EMail").fill("testauto222@gmail.com")
        page.get_by_placeholder("Enter Phone").fill("345435345")
        page.get_by_placeholder("Start Date").fill("2026-08-22")
        page.get_by_placeholder("End Date").fill("2026-08-25")
        page.get_by_label("Address:").fill("Flat no- 202, NKD Society, Delhi, India, 876653")
        

        page.get_by_text("male").nth(0).click()
        
        page.locator("#sunday").check()
        page.locator("#saturday").check()
        page.wait_for_timeout(1000)

        page.locator("//select[@id='country']").select_option("india")
        page.locator("//select[@id='country']").scroll_into_view_if_needed()

        page.locator("#colors").select_option(["red", "green"])
        page.locator("#animals").select_option(["cat","Dog"])
        page.locator("#animals").scroll_into_view_if_needed()

        page.locator("input#datepicker").fill("08/25/2026")
        page.locator("input#txtDate").click()
        page.locator("a[data-date='29']").click()

        page.locator("input#start-date").type("08/25/2026")
        page.locator("input#end-date").type("08/27/2026")
        page.locator("button.submit-btn").click()
        print("Date Msg:", page.locator("#result").inner_text())

        page.locator("input#singleFileInput").set_input_files("TestData/Testdata1.txt")
        page.locator("//button[@type='submit'and text()='Upload Single File']").click()
        print("File Uploaded:", page.locator("p#singleFileStatus").inner_text())

        file1 = "TestData/Testdata2.txt"
        file2 = "TestData/Testdata3.docx"
        file3 = "TestData/testdata4.pdf"
        file4 = "TestData/testdata5.xlsx"
        
        page.locator("input#multipleFilesInput").set_input_files([file1, file2, file3, file4])
        page.locator("//button[@type='submit'and text()='Upload Multiple Files']").click()
        page.locator('[id="multipleFilesInput"]').scroll_into_view_if_needed
        print("Files Uploaded:", page.locator("p#multipleFilesStatus").inner_text())
        page.locator("p#multipleFilesStatus").scroll_into_view_if_needed()
        #print("Table Value:", page.locator("//[@td='Learn Selenium']").text_content())
        #print("Table Value:", page.get_by_role("cell", name="Learn Selenium").text_content())
        #print("Cell Values:", )

        #page.evaluate("window.scrollBy(0, 700)")
        #time.sleep(2)
        
BrowserElements()

