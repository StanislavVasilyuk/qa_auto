import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://github.com/login")
    login_field=driver.find_element(By.ID, "login_field")
    login_field.send_keys("sergiibutenko@ukr.nettt")
    pass_field=driver.find_element(By.ID, "password")
    pass_field.send_keys("xxxxxxxxxxxx")
    button_login=driver.find_element(By.NAME, "commit") 
    button_login.click()
    assert driver.title=="Sign in to GitHub · GitHub"
    time.sleep(3)
    driver.close()
