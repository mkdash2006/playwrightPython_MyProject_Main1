from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression2
def test_pageassert01(page):
        page.goto("https://testautomationpractice.blogspot.com/", timeout=60000)
        expect(page.locator("#name")).to_be_visible(timeout=2000)
        expect(page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]")).to_have_text("Learn Selenium")
        expect(page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]")).to_contain_text("Learn Selenium")

@pytest.mark.regression2
def test_handle_alerts_lamda01(page):
        page.goto("https://testautomationpractice.blogspot.com/", timeout=6000)
        # Function with Lamda
        page.on("dialog", lambda dialog: dialog.dismiss())
        page.locator("button#confirmBtn").click()

@pytest.mark.regression2
def test_childpage01(page):
        page.goto("https://testautomationpractice.blogspot.com/", timeout=10000)
        with page.expect_popup() as cp:
            page.locator("[onclick='myFunction()']").click()
        page2 = cp.value
        print(page2.title())

@pytest.mark.regression2
def test_grabcellvalue01(page):
        page.goto("https://testautomationpractice.blogspot.com/")  
        val= page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]").text_content() 
        print("1st Cell Data:", val)

@pytest.mark.regression2
def test_grabrowvalue01(page):
        page.goto("https://testautomationpractice.blogspot.com/")
        # Static Web Table
        l1=[]
        for i in range(1,5):
            val= page.locator(f"//table[@name='BookTable']/tbody/tr[2]/td[{i}]").text_content()
            l1.append(val)
        print("1st Row Data:", l1)

@pytest.mark.regression2
def test_grabtabledata01(page):
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

@pytest.mark.regression2
def test_iframework01(page):
        page.goto("https://demo.guru99.com/test/guru99home/", timeout=50000)
        dd=page.frame_locator("//iframe[contains(@src, 'https://www.youtube.com/embed')]")
        dd.locator("button.ytmCuedOverlayPlayButton").click()




