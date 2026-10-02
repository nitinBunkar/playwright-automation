from playwright.sync_api import Page, expect


def test_login_ticket(logged_inpage: Page):
    # Validate successful navigation
    expect(logged_inpage).to_have_url(
        "https://rahulshettyacademy.com/angularpractice/shop"
    )


def test_add_iphone(logged_inpage: Page):

    """iphone_locator = logged_inpage.locator(
        "xpath=/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[1]/div/div[2]/button"
    )
    """
    iphone_locator = logged_inpage.locator("app-card").filter(has_text="iphone X")
    iphone_locator.get_by_role("button",name="Add").click()

    """samsung_locator = logged_inpage.locator(
        "xpath=/html/body/app-root/app-shop/div/div/div[2]/app-card-list/app-card[2]/div/div[2]/button"
    )
    """
    samsung_locator = logged_inpage.locator("app-card").filter(has_text="Samsung Note 8")
    samsung_locator.get_by_role("button",name="Add").click()

    logged_inpage.get_by_text("Checkout", exact=False).click()

    # Validate checkout page
    expect(logged_inpage.get_by_text("Checkout", exact=False)).to_be_visible()

    cart_items = logged_inpage.locator("tbody tr").filter(has=logged_inpage.locator("td"))
    expect(cart_items).to_have_count(4)



