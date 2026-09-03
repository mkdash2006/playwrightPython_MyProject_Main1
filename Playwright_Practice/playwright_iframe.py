from playwright.sync_api import sync_playwright, expect

def Test_iframework():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.guru99.com/test/guru99home/", timeout=0000)
        #page.wait_for_timeout(2000)
        #page.frame_locator("//iframe[contains(@src,'youtybe')]").get_by_title("Play video").click()
        # xyz = page.frame_locator("//iframe[@wmode]")
        # xyz.locator("button.ytmCuedOverlayPlayButton").click()
        #page.frame_locator("//iframe[@wmode]").locator("button.ytmCuedOverlayPlayButton").click()
        #dd = page.frame_locator("//iframe[contains(@src,'https://www.youtube.com/embed')]")
        #dd= page.frame_locator("//iframe[@wmode='transparent' and @src='https://www.youtube.com/embed/RbSlW8jZFe8']")
        dd=page.frame_locator("//iframe[contains(@src, 'https://www.youtube.com/embed')]")
        dd.locator("button.ytmCuedOverlayPlayButton").click()
        page.wait_for_timeout(6000)

Test_iframework()

