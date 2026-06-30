from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Создать объект страницы авторизации.

        Args:
            driver: экземпляр WebDriver.

        Returns:
            None.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """
        Открыть страницу авторизации.

        Returns:
            None.
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Ввести логин, пароль и нажать кнопку входа.

        Args:
            username: имя пользователя.
            password: пароль пользователя.

        Returns:
            None.
        """
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
