import pytest
from playwright.sync_api import sync_playwright
import support.selectors as sel

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_saucedemo(browser):
    page = browser

    # Test Case 1: Login with valid credentials
    page.goto(sel.login_url)
    page.fill(sel.username_field, "standard_user")
    page.fill(sel.password_field, "secret_sauce")
    page.click(sel.login_button)

    assert page.url == sel.inventory_url
    assert page.is_visible(sel.inventory_list)

    # Test Case 2: Add first item to Cart 
    page.click(sel.first_add_to_cart_button)

    assert page.text_content(sel.cart_badge) == "1"
    page.click(sel.cart_link)
    assert page.is_visible(sel.first_remove_button)

    # Test Case 4: Checkout
    page.click(sel.checkout_button)
    page.fill(sel.first_name_field, "Ilia")
    page.fill(sel.last_name_field, "Shliapin")
    page.fill(sel.postal_code_field, "08001")
    page.click(sel.continue_button)
    page.click(sel.finish_button)

    assert page.is_visible(sel.thank_you_message)
