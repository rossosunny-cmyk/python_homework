from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CheckoutPage:
    """Page Object для страницы оформления заказа SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Создать объект страницы оформления заказа.

        Args:
            driver: экземпляр WebDriver.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        """
        Заполнить форму оформления заказа.

        Args:
            first_name: имя покупателя.
            last_name: фамилия покупателя.
            postal_code: почтовый индекс.

        Returns:
            None.
        """
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_checkout(self) -> None:
        """
        Нажать кнопку Continue.

        Returns:
            None.
        """
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Получить итоговую стоимость заказа.

        Returns:
            Текст итоговой стоимости заказа.
        """
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        ).text
