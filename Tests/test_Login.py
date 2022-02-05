from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/LENOVO/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)  # for accessing all the functions from LoginPage Class
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.Click_login()

        # Making Object from HomePage Model
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Was Successfull")