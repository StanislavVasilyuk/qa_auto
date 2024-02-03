from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    URL='https://github.com/login'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)
    def try_login (self, username, password):
        login_field=self.driver.find_element(By.ID, "login_field")
        login_field.send_keys(username)
        pass_field=self.driver.find_element(By.ID, "password")
        pass_field.send_keys(password)
        button_login=self.driver.find_element(By.NAME, "commit") 
        button_login.click()
    def check_title (self, expected_title):
        return self.driver.title==expected_title