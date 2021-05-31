from selenium.webdriver.common.by import By

class HomeActivity:

    def __init__(self, driver):
        self.driver = driver

        # Welcome message
        self.welcomeMessage = 'io.grainchain.logintest:id/textview_first'


    def get_welcome_text(self):
        """
        Get the text displayed in the home page after login
        """
        welcomeText = self.driver.find_element_by_id(self.welcomeMessage)
        return welcomeText.text