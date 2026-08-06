from playwright.sync_api import Playwright, expect

from utils.BaseApi import APIBASE


def test_webapi(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api = APIBASE()
    orderId = api.create_order(playwright)

    print(orderId)
#     Login
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill("jatin2485@gmail.com")
    page.locator("#userPassword").fill("Qwerty@1234")
    page.locator("#login").click()



    page.get_by_role("button",name="Orders").click()
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()
