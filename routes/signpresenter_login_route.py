
import time

import pyautogui

def signpresenter_login_route(page, email, password):
  print("Attempting to login to signpresenter..")
  page.goto('https://admin.signpresenter.com/login')
  page.wait_for_load_state('load')
  page.type('input#email', email)
  page.type('input#password', password)
  page.click('button#signInButton')
  page.wait_for_selector('i.fa-caret-down')
  print('Signpresenter loaded')
  return page

