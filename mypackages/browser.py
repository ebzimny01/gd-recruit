from playwright.sync_api import sync_playwright


class WISPage:
    def __init__(self, page):
        self.page = page

    def login(self, config):
        username = config['WISCreds']['username']
        password = config['WISCreds']['password']

        self.page.set_viewport_size({"width": 1900, "height": 1200})
        self.page.goto("http://idsrv.fanball.com/")
        print(self.page.title())
        
        print("Authenticating to WIS...")
        
        # Click input[name="username"]
        self.page.click("input[name=\"username\"]")
        # Fill input[name="username"]
        self.page.fill("input[name=\"username\"]", username)
        
        # Click input[name="password"]
        self.page.click("input[name=\"password\"]")
        # Fill input[name="password"]
        self.page.fill("input[name=\"password\"]", password)
        
        # Click button:has-text("Sign in")
        self.page.click("button:has-text(\"Sign in\")")

        check_auth = self.page.text_content("Incorrect email or password", timeout=2000)
        print(f"Value of check_auth = {check_auth}")

        if check_auth is None:
            return True
        else:
            return False

def get_browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        wispage = WISPage(page)
        return browser, wispage
