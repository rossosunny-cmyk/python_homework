import allure
from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from login_page import LoginPage
from main_shop_page import MainShopPage


@allure.title("Проверка покупки в интернет-магазине")
@allure.description("Проверка итоговой суммы заказа в SauceDemo.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Открыть браузер Firefox"):
        driver = webdriver.Firefox()

    with allure.step("Создать Page Object"):
        login_page = LoginPage(driver)
        main_shop_page = MainShopPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

    with allure.step("Открыть сайт магазина"):
        login_page.open()

    with allure.step("Авторизоваться как standard_user"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        main_shop_page.add_backpack()
        main_shop_page.add_bolt_t_shirt()
        main_shop_page.add_onesie()

    with allure.step("Перейти в корзину"):
        main_shop_page.open_cart()

    with allure.step("Нажать Checkout"):
        cart_page.checkout()

    with allure.step("Заполнить данные покупателя"):
        checkout_page.fill_form("Алеся", "Ломакина", "123456")
        checkout_page.continue_checkout()

    with allure.step("Получить итоговую стоимость"):
        total = checkout_page.get_total()

    with allure.step("Закрыть браузер"):
        driver.quit()

    with allure.step("Проверить итоговую сумму"):
        assert total == "Total: $58.29"
