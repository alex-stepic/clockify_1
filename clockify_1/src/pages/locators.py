from selenium.webdriver.common.by import By

class ProfilePageLocators():
    AVATAR_IMG = (By.CSS_SELECTOR, "avatar.cl-upload-img>img")
    UPPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "btn-upload-file>label.cl-btn")
    FILE_NAME=(By.CSS_SELECTOR,'input[type = "file"]')
    AVATAR_IMG=(By.CSS_SELECTOR,'div.cl-page-wrapper avatar.cl-upload-img>img[class*="avatar"]')
    AVATAR_IMG_HEADER = (By.CSS_SELECTOR, 'div#topbar-menu avatar>img[class*="avatar"]')

class LoginPageLocators():
    LOGIN_NAME = (By.CSS_SELECTOR, "input#email")
    PASSWORD = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

