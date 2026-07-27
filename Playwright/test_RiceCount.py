from playwright.sync_api import Page, expect


def test_rice (page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            pricecolvalue = index
            print(f"Price column value is {pricecolvalue}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(pricecolvalue)).to_have_text("37")



