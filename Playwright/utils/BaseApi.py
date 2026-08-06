from playwright.sync_api import Playwright

orderPlaced = {"orders":[{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}
class APIBASE:

    def get_token(self,playwright:Playwright):
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response =api_req_context.post(url="/api/ecom/auth/login",
                             data={"userEmail": "jatin2485@gmail.com", "userPassword": "Qwerty@1234"}
                             )
        response_json = response.json()
        token = response_json["token"]
        print(token)
        return token

    def create_order(self,playwright:Playwright):
        token = self.get_token(playwright)
        api_req_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_req_context.post(url="/api/ecom/order/create-order",
                                        data= orderPlaced,

                                        headers = {"Authorization": token,
                                                   "Content-Type": "application/json"}
                                        )
        print(response.json())
        response_body = response.json()

        orderId = response_body["orders"][0]
        return orderId

