import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from signup_page import SignupPage


def test_signup():

    driver = webdriver.Chrome()

    try:

        driver.maximize_window()

        signup = SignupPage(driver)

        signup.open()

        phone_number = "9" + str(int(time.time()))[-9:]

        # Generate unique email every run
        test_email = f"qa{int(time.time())}@example.com"

        signup.signup(
            first_name="Abishek",
            last_name="Durao",
            phone=phone_number,
            email=test_email,
            password="Test123@",
            confirm_password="Test123@"
        )

        print("Generated Phone:", phone_number)
        print("Generated Email:", test_email)

        print("Waiting for Verify Account page...")

        verify_email = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.ID, "verifEmail")
            )
        )

        displayed_email = verify_email.get_attribute("value")

        print("Displayed Email:", displayed_email)

        assert displayed_email == test_email

        resend_button = driver.find_element(
            By.XPATH,
            "//button[contains(text(),'Resend Verification')]"
        )

        assert resend_button.is_displayed()

        print("\nTC_SIGNUP_001 PASSED")
        print("Verify Account page displayed successfully")

    except Exception as e:

        print("\nTC_SIGNUP_001 FAILED")
        print(e)

    finally:

        input("\nPress Enter to close browser...")
        driver.quit()


if __name__ == "__main__":
    test_signup()