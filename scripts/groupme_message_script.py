import os

from playwright.sync_api import Playwright, sync_playwright

from routes import groupme_login_route
from routes import groupme_message_route

def groupme_message_script(options):

  account = options['account']
  groupme_message = options['message']
  headless = options['headless']

  username = os.environ['GROUPME_USERNAME']
  password = os.environ['GROUPME_PASSWORD']

  if account == 'test':
    chat_labels = ['Automation Testing']

  if account == 'southroads':
    chat_labels = ['Southroads Leadership']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = groupme_login_route(page, username, password)
    page = groupme_message_route(page, chat_labels, groupme_message)
