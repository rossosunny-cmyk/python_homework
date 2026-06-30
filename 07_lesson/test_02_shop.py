from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from login_page import LoginPage
from main_shop_page import MainShopPage


def test_shop():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    main_shop_page = MainShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_shop_page.add_backpack()
    main_shop_page.add_bolt_t_shirt()
    main_shop_page.add_onesie()
    main_shop_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_form("Алеся", "Ломакина", "123456")
    checkout_page.continue_checkout()
    total = checkout_page.get_total()

    driver.quit()

    assert total == "Total: $58.29"
