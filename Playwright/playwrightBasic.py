import time

from paste.deploy.converters import falsy
from playwright.sync_api import Page, expect , Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context() # do some operation, login ->
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    # page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_label("Password").fill("Learning@830$3mK2")

    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_firefoxBasics(playwright:Playwright):
    firefoxbroswer = playwright.firefox.launch(headless=False)
    page = firefoxbroswer.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    # page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_label("Password").fill("Learning@830$3mK21531")

    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
