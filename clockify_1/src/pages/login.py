from .base import BasePage
from .profile import ProfilePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def login_user(self, name, password):

            while not self.is_element_present(*LoginPageLocators.LOGIN_NAME):
                 time.sleep(3)

            xname = self.browser.find_element(*LoginPageLocators.LOGIN_NAME)
            xname.clear()
            xname.send_keys(name)
            time.sleep(1)

            xpassword = self.browser.find_element(*LoginPageLocators.PASSWORD)
            xpassword.clear()
            xpassword.send_keys(password)
            time.sleep(1)

            xbutton = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
            time.sleep(1)
            xbutton.click()
            time.sleep(1)
            return ProfilePage(browser=self.browser, url=self.browser.current_url)

