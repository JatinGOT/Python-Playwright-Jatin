import json

import pytest
from playwright.sync_api import Playwright, expect

from PageObject.Login import LoginPage
from PytestPython.PytestPython.playwright.conftest import user_credentials
from utils.apiBase import BaseApi


#   Json file ->utils ->access into test

with open('Data/credentials.json') as f:
        test_data = json.load(f)
        print(test_data)
        user_credentials = test_data["userCredentials"]


@pytest.mark.parametrize('userCredentials',user_credentials)

def test_api(playwright:Playwright ,userCredentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Create Order Id
    api = BaseApi()
    order_Id =  api.createOrder(playwright , userCredentials)

    # Log In
    loginPage = LoginPage(page)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(userCredentials["name"])
    page.locator("#userPassword").fill(userCredentials["password"])
    page.locator("#login").click()

# Order ID Summary
    page.get_by_role("button",name="Orders").click()
    row = page.locator("tr").filter(has_text=order_Id)
    row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()


