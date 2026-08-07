from .Dashboard import Dashboard


class LoginPage:
    def __init__(self,page):
        self.page = page


    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def LoginPage(self, username,password):
        self.page.get_by_placeholder("email@example.com").fill(username)
        self.page.locator("#userPassword").fill(password)
        self.page.locator("#login").click()
        dashboard = Dashboard(self.page)
        return dashboard

