from .base import BasePage
from .locators import LoginPageLocators
from .locators import ProfilePageLocators
from src.utilties import *
import time


class ProfilePage(BasePage):

    def is_profile_open(self):
        if self.is_element_present(*ProfilePageLocators.AVATAR_IMG):
            return True
        else:
            return False
    def check_update_avatar(self,xfile):
        xname_file=self.browser.find_element(*ProfilePageLocators.FILE_NAME)
        xname_file.send_keys(avatar_full(xfile))
        time.sleep(5)
        xreal=self.get_avatar_name()
        assert xreal==xfile, f"Аватарка в профиле.Expect -{xfile}. Real - {xreal}"
        xreal = self.get_header_avatar_name()
        assert xreal == xfile, f"Аватарка в хедере.Expect -{xfile}. Real - {xreal}"
    def check_update_avatar_neg(self,xfile):
        xold = self.get_avatar_name()
        xold_header=self.get_header_avatar_name()
        xname_file=self.browser.find_element(*ProfilePageLocators.FILE_NAME)
        xname_file.send_keys(avatar_full_neg(xfile))
        time.sleep(5)
        xreal=self.get_avatar_name()
        assert xreal==xold, f"Аватарка в профиле.Expect -{xold}. Real - {xreal}"
        xreal = self.get_header_avatar_name()
        assert xreal==xold_header, f"Аватарка в хедере.Expect -{xold}. Real - {xreal}"
    def get_avatar_name(self):
        xlink=self.browser.find_element(*ProfilePageLocators.AVATAR_IMG)
        return xlink.get_attribute("src")[-9:] # в тестовых даннных имя аватарки -последние 9 символов
    def get_header_avatar_name(self):
        xlink=self.browser.find_element(*ProfilePageLocators.AVATAR_IMG_HEADER)
        return xlink.get_attribute("src")[-9:] # в тестовых даннных имя аватарки -последние 9 символов