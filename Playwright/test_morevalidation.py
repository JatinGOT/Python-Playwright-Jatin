import time
from collections import namedtuple

from playwright.sync_api import  Page,expect


def test_uicheck(page : Page):
    # Hide and pop up
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)


    # Alerts basic
    page.on("dialog", lambda  dialog:dialog.accept())
    page.get_by_role("button",name="Confirm").click()

    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    # Frame Handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link",name = "All Access plan").click()
    time.sleep(2)
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")



