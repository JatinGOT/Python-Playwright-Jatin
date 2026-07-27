import time

from playwright.sync_api import Page, expect


def test_dynamicvalidation(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").click()
    page.get_by_role("button", name="Sign In").click()

# Search Iphone
    iphoneProduct = page.locator(".card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
# Search Blueberry
    blueberryProduct = page.locator(".card").filter(has_text="Blackberry")
    blueberryProduct.get_by_role("button").click()

# Check out Click
    page.locator(".nav-link").filter(has_text="Checkout").click()
    time.sleep(2)

# Check if the write product are showing or it  counts is shows correct or not
    expect(page.get_by_text("iphone X")).to_be_visible()
    expect(page.get_by_text("Blackberry")).to_be_visible()

    expect(page.locator(".media")).to_have_count(2)



def test_childwindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as popup_info:
        page.locator(".blinkingText").filter(has_text="Free Access to InterviewQues/ResumeAssistance/Material").click()

        childPage = popup_info.value

        text = childPage.locator(".red").text_content()

        print(text)
        email = text.split("at")
        emailText = email[1].strip().split(" ")[0]
        print("Email :" , emailText)
        assert emailText == "mentor@rahulshettyacademy.com"
