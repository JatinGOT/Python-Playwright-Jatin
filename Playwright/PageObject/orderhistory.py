from .orderDetails import OrderDetailsPage


class OrderHistory:

    def __init__(self,page):
        self.page = page

    def selectOrder(self,order_Id):
        row = self.page.locator("tr").filter(has_text=order_Id)
        row.get_by_role("button", name="View").click()
        orderDetails = OrderDetailsPage(self.page)
        return orderDetails