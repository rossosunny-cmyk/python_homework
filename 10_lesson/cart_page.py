from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:
    """Page Object для страницы корзины SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Создать объект страницы корзины.

        Args:
            driver: экземпляр WebDriver.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self) -> None:
        """
        Нажать кнопку Checkout.

        Returns:
            None.
        """
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
