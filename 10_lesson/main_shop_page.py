from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainShopPage:
    """Page Object для главной страницы магазина SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Создать объект главной страницы магазина.

        Args:
            driver: экземпляр WebDriver.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self) -> None:
        """
        Добавить товар Sauce Labs Backpack в корзину.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, "add-to-cart-sauce-labs-backpack")
            )
        ).click()

    def add_bolt_t_shirt(self) -> None:
        """
        Добавить товар Sauce Labs Bolt T-Shirt в корзину.

        Returns:
            None.
        """
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt",
        ).click()

    def add_onesie(self) -> None:
        """
        Добавить товар Sauce Labs Onesie в корзину.

        Returns:
            None.
        """
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-onesie",
        ).click()

    def open_cart(self) -> None:
        """
        Перейти в корзину.

        Returns:
            None.
        """
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
