from playwright.sync_api import sync_playwright

p = sync_playwright().start()
browser = p.firefox.launch(headless=False)
page = browser.new_page()
page.goto("https://www.whatifsports.com")
print(page.title())
page.pause()
browser.close()
p.stop()