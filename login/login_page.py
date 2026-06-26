from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = "https://tichi-app-webapp-stage.web.app/login"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email_field.clear()
        email_field.send_keys(email)

    def click_continue(self):
        btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@type='submit']")
            )
        )
        btn.click()

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def login(self, email, password):
        self.open()
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_continue()