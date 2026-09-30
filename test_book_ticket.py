

from playwright.sync_api import Page

def test_book_ticket(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    ##close_button = page.locator('//*[@id="header-container"]/div[2]/div[2]/div/section/span')
    ##page.pause()
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox").check()
    page.locator("#signInBtn").click()
    page.on("dialog", lambda dialog: dialog.accept())

def test_add_iphone(logged_inpage:Page):

    iphone_locator = logged_inpage.locator("xpath=/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[1]/div/div[2]/button")
    iphone_locator.click()

    samsung_locator = logged_inpage.locator("xpath=/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[2]/div/div[2]/button")
    samsung_locator.click()

    #logged_inpage.get_by_role("button",name ="Checkout").click()
    logged_inpage.get_by_text("Checkout", exact=False).click()
