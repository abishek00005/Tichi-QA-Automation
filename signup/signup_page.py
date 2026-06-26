from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    URL = "https://tichi-app-webapp-stage.web.app/sign-up"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)

    def signup(
        self,
        first_name,
        last_name,
        phone,
        email,
        password,
        confirm_password
    ):

        self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "firstName")
            )
        ).send_keys(first_name)

        self.driver.find_element(
            By.ID,
            "lastName"
        ).send_keys(last_name)

        self.driver.find_element(
            By.ID,
            "phoneNumber"
        ).send_keys(phone)

        self.driver.find_element(
            By.ID,
            "email"
        ).send_keys(email)

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

        self.driver.find_element(
            By.ID,
            "confirmPassword"
        ).send_keys(confirm_password)

        # Accept Terms & Conditions
        self.driver.find_element(
            By.ID,
            "remember"
        ).click()

        # Click Sign Up
        signup_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        )

        signup_button.click()