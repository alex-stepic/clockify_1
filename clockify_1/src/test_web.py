import json
import pytest
from selenium import webdriver
from src.pages.login import LoginPage
from src.pages.profile import ProfilePage
from src.utilties import *
import os
import time

with open(global_par(),'r', encoding="utf-8") as f:
    data = json.loads(f.read())
    link = data["link"]
    link_profile = data["link_profile"]
    link_login = data["link_login"]
    user_name = data["user_name"]
    password = data["password"]

json_filepath = os.path.join('.', 'src', 'global.json')
print("*"+json_filepath+".")

@pytest.fixture(scope="module")
def browser():
    # Инициализация ChromeDriver
    browser = webdriver.Chrome()
    browser.delete_all_cookies()

    page = ProfilePage(browser,link)
    page.open()
    if not page.is_profile_open():
       page=LoginPage(browser,link_login)
       page.login_user(user_name, password)

    yield browser
    browser.quit()
@pytest.mark.parametrize('ximage',avatar_set())
def test_update_avatar(browser,ximage):
     page = ProfilePage(browser,link_profile)
     page.open()
     browser.maximize_window()
     time.sleep(3)
     page.check_update_avatar(ximage)
     time.sleep(1)
@pytest.mark.parametrize('ximage',bad_avatar_set())
def test_update_avatar_negative(browser,ximage):
     page = ProfilePage(browser,link_profile)
     page.open()
     browser.maximize_window()
     time.sleep(3)
     page.check_update_avatar_neg(ximage)
     time.sleep(1)