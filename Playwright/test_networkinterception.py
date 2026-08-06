from playwright.async_api import Page
from playwright.sync_api import Playwright, expect

from utils.apiBase import BaseApi

fakepayloadresponse = {"data":[],"message":"No Orders"}
def fakePayload(route):
    route.fulfill(
        json = fakepayloadresponse
    )


def test_networkFakeResponse(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-count/*",fakePayload)
    page.get_by_placeholder("email@example.com").fill("jatin2485@gmail.com")
    page.locator("#userPassword").fill("Qwerty@1234")
    page.locator("#login").click()

    page.get_by_role("button", name="Orders").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)



def fakeRequest(route):
    route.continue_(
        url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6a69a16b85b8849b49186780"
    )


def test_networkFakeResponse2(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", fakeRequest)
    page.get_by_placeholder("email@example.com").fill("jatin2485@gmail.com")
    page.locator("#userPassword").fill("Qwerty@1234")
    page.locator("#login").click()

    page.get_by_role("button", name="Orders").click()
    page.get_by_role("button",name="view").first.click()

    message = page.locator(".blink_me").text_content()
    print(message)

def test_sessionToken(playwright:Playwright):

    api = BaseApi()
    token = api.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token','{token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name = "ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()