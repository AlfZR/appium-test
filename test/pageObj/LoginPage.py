from selenium.webdriver.common.by import By

class LoginActivity:

    def __init__(self, driver):
        self.driver = driver

        # Inputs
        self.email = 'io.grainchain.logintest:id/username'
        self.password = 'io.grainchain.logintest:id/password'

        # Sign in or register button
        self.signIn = 'io.grainchain.logintest:id/login'

    def enterEmail(self, email):
        """
        Enter an email in the email input
        """
        emailInput = self.driver.find_element_by_id(self.email)
        emailInput.clear()
        emailInput.send_keys(email)
        print('Email set')

    def enterPassword(self, password):
        """
        Enter a password in the password input
        """
        passwordInput = self.driver.find_element_by_id(self.password)
        passwordInput.clear()
        passwordInput.send_keys(password)
        print('Password set')

    def clickSignInButton(self):
        """
        Click on the sigin button
        """
        signInBtn = self.driver.find_element_by_id(self.signIn)
        signInBtn.click()

    def get_email(self):
        """
        Get the email set in the email input
        """
        emailText = self.driver.find_element_by_id(self.email)
        return emailText.text

    def get_button_status(self):
        """
        Get the current status of the sign in button
        """
        signInBtn = self.driver.find_element_by_id(self.signIn)
        return signInBtn.is_enabled()