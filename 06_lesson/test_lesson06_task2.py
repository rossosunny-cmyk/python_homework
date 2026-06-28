from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


BASE_URL = "https://gitflic.ru/"

USER_1_PROFILE_URL = "https://gitflic.ru/user/PASTE_USER_1"
USER_2_PROFILE_URL = "https://gitflic.ru/user/PASTE_USER_2"

USER_1_COOKIES = [
    {
        "name": "PASTE_COOKIE_NAME_USER_1",
        "value": "PASTE_COOKIE_VALUE_USER_1",
        "path": "/",
    },
]

USER_2_COOKIES = [
    {
        "name": "PASTE_COOKIE_NAME_USER_2",
        "value": "PASTE_COOKIE_VALUE_USER_2",
        "path": "/",
    },
]


def add_cookies(driver, cookies):
    for cookie in cookies:
        driver.add_cookie(cookie)


def cookies_are_applied(driver, cookies):
    for cookie in cookies:
        added_cookie = driver.get_cookie(cookie["name"])
        if added_cookie is None:
            return False
        if added_cookie["value"] != cookie["value"]:
            return False
    return True


def open_profile_with_cookies(driver, cookies, profile_url):
    driver.get(BASE_URL)
    driver.delete_all_cookies()
    add_cookies(driver, cookies)

    cookies_applied = cookies_are_applied(driver, cookies)

    driver.refresh()
    driver.get(profile_url)

    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    return driver.current_url, cookies_applied


def test_session_storage_auth():
    driver = webdriver.Chrome()

    user_1_url, user_1_cookies_applied = open_profile_with_cookies(
        driver,
        USER_1_COOKIES,
        USER_1_PROFILE_URL,
    )

    driver.delete_all_cookies()
    driver.get(BASE_URL)

    user_2_url, user_2_cookies_applied = open_profile_with_cookies(
        driver,
        USER_2_COOKIES,
        USER_2_PROFILE_URL,
    )

    driver.quit()

    assert user_1_cookies_applied is True
    assert user_2_cookies_applied is True
    assert user_1_url != user_2_url
