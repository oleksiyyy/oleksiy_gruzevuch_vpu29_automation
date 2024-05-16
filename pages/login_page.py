import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_url_not_contains_logged_in_successfully(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        current_url = self.driver.current_url
        self.assertNotIn("logged-in-successfully", current_url, "URL contains 'logged-in-successfully'")

    def test_login_and_logout(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        submit_button = self.driver.find_element(By.ID, "submit")

        username_field.send_keys("student")
        password_field.send_keys("Password123")

        submit_button.click()

        logout_button = self.driver.find_element(By.ID, "logout")
        logout_button.click()

        current_url = self.driver.current_url
        self.assertNotIn("logged-in-successfully", current_url, "URL contains 'logged-in-successfully'")


if __name__ == "__main__":
    unittest.main()