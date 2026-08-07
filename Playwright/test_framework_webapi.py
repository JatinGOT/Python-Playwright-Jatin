import json

import pytest
from playwright.sync_api import Playwright, expect

from PageObject.Login import LoginPage
from PageObject.Dashboard import Dashboard
from PageObject import orderhistory
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
    username = userCredentials["name"]
    password = userCredentials["password"]

    loginPage = LoginPage(page)
    loginPage.navigate()

    dashboard = loginPage.LoginPage(username,password)
    orderhistoryPage =dashboard.orderclick()
    orderDetailsPage = orderhistoryPage.selectOrder(order_Id)
    orderDetailsPage.verifyPage()
    context.close()


