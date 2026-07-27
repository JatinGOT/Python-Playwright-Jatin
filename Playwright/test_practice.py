import time
from playwright.sync_api import Page , Playwright, expect
def test_p (playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # do some operation, login ->
    page = context.new_page()


def test_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("Jatinbm@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Jatinbm@gmail.com")
    page.locator("#login").click()

    expect(page.get_by_text("Incorrect email or passwcxzczxczxord.")).to_be_visible()
    time.sleep(5)