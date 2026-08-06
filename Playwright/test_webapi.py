from playwright.sync_api import Playwright, expect

from utils.apiBase import BaseApi

def test_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Create Order ID
    api = BaseApi()
    order_Id =  api.createOrder(playwright)



    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("jatin2485@gmail.com")
    page.locator("#userPassword").fill("Qwerty@1234")
    page.locator("#login").click()

# Order ID Summary
    page.get_by_role("button",name="Orders").click()
    row = page.locator("tr").filter(has_text=order_Id)
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()


