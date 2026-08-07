from .orderhistory import OrderHistory


class Dashboard:

    def __init__(self,page):
        self.page = page

    def orderclick(self):
        self.page.get_by_role("button", name="Orders").click()
        orderHistoryPage = OrderHistory(self.page)
        return orderHistoryPage