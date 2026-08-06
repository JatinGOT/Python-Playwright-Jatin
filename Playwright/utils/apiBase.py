
from playwright.sync_api import Playwright

order_placed = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}
class BaseApi:


    def get_token(self,playwright:Playwright , userCredentials):
        USER_EMAIL = userCredentials["name"]
        USER_PASSWORD = userCredentials["password"]
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post(url="/api/ecom/auth/login",
                                        data={
                                            "userEmail": USER_EMAIL, "userPassword": USER_PASSWORD
                                        })
        response_json = response.json()
        token = response_json["token"]
        print(token)
        return  token


    def createOrder(self,playwright:Playwright , userCredentials):
        token = self.get_token(playwright, userCredentials)
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_req_context.post(url="/api/ecom/order/create-order",
                                        data = order_placed,
                                        headers= {"Authorization" : token,
                                                  "Content-Type" : "application/json"})

        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId




