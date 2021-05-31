from appium import webdriver
import unittest
from pageObj.LoginPage import LoginActivity
from pageObj.HomePage import HomeActivity
from time import sleep

class Conection(unittest.TestCase):

    def setUp(self):
        self.driver = {
            "platformName": "android",
            "platformVersion": "11.0",
            "deviceName": "pixel",
            "noReset": "True",
            "appPackage": "io.grainchain.logintest",
            "appActivity": ".ui.login.LoginActivity",
            "automationName": "uiautomator2",
            "app": "C:\\Users\\Alfonso\\Documents\\GrainApp\\app-debug.apk"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.driver)
        self.loginMainPage = LoginActivity(self.driver)
        self.homeMainPage = HomeActivity(self.driver)

        self.userName = 'abc123'
        self.passW = '123456'
        self.invalidPassW = '1234'


    # Check if the password not fill the length, the sign in button is disabled
    def test_one_disabled_button(self):
        self.loginMainPage.enterEmail(self.userName)
        self.loginMainPage.enterPassword(self.invalidPassW)
        self.assertFalse(self.loginMainPage.get_button_status())
        print('Button validated')

    # Login process with valid email and password
    def test_two_successfull_login(self):
        self.loginMainPage.enterEmail(self.userName)
        self.loginMainPage.enterPassword(self.passW)
        self.loginMainPage.clickSignInButton()
        print('Login successfull')

    # Check that the username in the TextView is the text introduced in the username field
    def test_three_welcome_message(self):
        self.loginMainPage.enterEmail(self.userName)
        email = self.loginMainPage.get_email()
        self.loginMainPage.enterPassword(self.passW)
        self.loginMainPage.clickSignInButton()
        sleep(3)
        welcome = self.homeMainPage.get_welcome_text()
        
        self.assertIn(email, welcome)
        print('Login successfull, welcome message validated')

if __name__ == '__main__':
    unittest.main()