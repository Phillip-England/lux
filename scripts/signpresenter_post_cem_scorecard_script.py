import os
import time

from playwright.sync_api import Playwright, sync_playwright

from routes import signpresenter_login_route
from routes import signpresenter_select_account_route
from routes import signpresenter_update_message_route

def signpresenter_post_cem_scorecard_script(options):

  account = options['account']
  headless = options['headless']

  if account == 'test':
    email = os.environ['SOUTHROADS_EMAIL']
    password = os.environ['SIGNPRESENTER_PASSWORD']
    file_path = os.path.join(os.environ['PROJECT_PATH'], 'images', 'cfa', f'{account}', 'cem_scorecard.jpg')

  if account == 'southroads':
    email = os.environ['SOUTHROADS_EMAIL']
    password = os.environ['SIGNPRESENTER_PASSWORD']
    file_path = os.path.join(os.environ['PROJECT_PATH'], 'images', 'cfa', f'{account}', 'cem_scorecard.jpg')

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = signpresenter_login_route(page, email, password)
    page = signpresenter_select_account_route(page, 'Chick-fil-A at Southroads')
    page = signpresenter_update_message_route(page, options={
      'message': 'TM Wallboard',
      'submessage': 'CEM Current Month',
      'file_path': file_path
    })