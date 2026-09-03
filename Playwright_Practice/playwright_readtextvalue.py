from playwright.sync_api import sync_playwright

### Read Cell value........................................

def grabcellvalue():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")  
        val= page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]").text_content() 
        print("1st Cell Data:", val)
grabcellvalue()

### Read Row Value.........................................

def grabrowvalue():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        # Static Web Table
        l1=[]
        for i in range(1,5):
            val= page.locator(f"//table[@name='BookTable']/tbody/tr[2]/td[{i}]").text_content()
            l1.append(val)
        print("1st Row Data:", l1)
grabrowvalue()

### Read Row Value......................................................

def grabtabledata():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        # Static Web Table
        # Find Rows  
        rows = page.locator("table[name='BookTable'] tr")
        # Loop Through Rows  
        for i in range(rows.count()):
            #Read Cells  
            cells = rows.nth(i).locator("td")
            #Store in List 
            row_values = [cells.nth(j).inner_text() for j in range(cells.count())]
            print("Table Data:", row_values)
grabtabledata()

