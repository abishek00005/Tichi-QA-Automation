from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage


VALID_EMAIL = "abishekdurao06@gmail.com"
VALID_PASSWORD = "Abishek006@@"


def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def print_result(tc_id, passed, error=""):
    if passed:
        print(f"{tc_id} PASSED")
    else:
        print(f"{tc_id} FAILED")
        if error:
            print(error)


# TC_LOGIN_001
def test_valid_login():
    driver = create_driver()

    try:
        login = LoginPage(driver)

        login.login(
            VALID_EMAIL,
            VALID_PASSWORD
        )

        WebDriverWait(driver, 10).until(
            EC.url_contains("/home")
        )

        assert "/home" in driver.current_url

        print_result("TC_LOGIN_001", True)

    except Exception as e:
        print_result("TC_LOGIN_001", False, str(e))

    finally:
        input("Press Enter to close browser...")
        driver.quit()


# TC_LOGIN_002
def test_invalid_password():
    driver = create_driver()

    try:
        login = LoginPage(driver)

        login.login(
            VALID_EMAIL,
            "WrongPass123@"
        )

        WebDriverWait(driver, 5).until(
            lambda d: "/home" not in d.current_url
        )

        assert "/home" not in driver.current_url

        print_result("TC_LOGIN_002", True)

    except Exception as e:
        print_result("TC_LOGIN_002", False, str(e))

    finally:
        input("Press Enter to close browser...")
        driver.quit()


# TC_LOGIN_003
def test_invalid_email():
    driver = create_driver()

    try:
        login = LoginPage(driver)

        login.open()

        login.enter_email("abc123")

        login.click_continue()

        password_fields = driver.find_elements(
            By.ID,
            "password"
        )

        assert len(password_fields) == 0

        print_result("TC_LOGIN_003", True)

    except Exception as e:
        print_result("TC_LOGIN_003", False, str(e))

    finally:
        input("Press Enter to close browser...")
        driver.quit()


# TC_LOGIN_004
def test_empty_email():
    driver = create_driver()

    try:
        login = LoginPage(driver)

        login.open()

        login.click_continue()

        password_fields = driver.find_elements(
            By.ID,
            "password"
        )

        assert len(password_fields) == 0

        print_result("TC_LOGIN_004", True)

    except Exception as e:
        print_result("TC_LOGIN_004", False, str(e))

    finally:
        input("Press Enter to close browser...")
        driver.quit()


# TC_LOGIN_005
def test_empty_password():
    driver = create_driver()

    try:
        login = LoginPage(driver)

        login.open()

        login.enter_email(VALID_EMAIL)

        login.click_continue()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.ID, "password")
            )
        )

        login.click_continue()

        assert "/home" not in driver.current_url

        print_result("TC_LOGIN_005", True)

    except Exception as e:
        print_result("TC_LOGIN_005", False, str(e))

    finally:
        input("Press Enter to close browser...")
        driver.quit()


if __name__ == "__main__":

    print("\nRunning Login Automation Tests\n")

    test_valid_login()
    test_invalid_password()
    test_invalid_email()
    test_empty_email()
    test_empty_password()

    print("\nExecution Completed\n")