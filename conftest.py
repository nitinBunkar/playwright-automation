import pytest
from playwright.sync_api import Page
@pytest.fixture
def logged_inpage(page :Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").check()
    page.locator("#signInBtn").click()
    page.on("dialog", lambda dialog: dialog.accept())
    return page

