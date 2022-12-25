from playwright.sync_api import Playwright, sync_playwright
from destinations import groupme
import os

def groupme_message(options):

  account = options['account']
  groupme_message = options['message']
  headless = options['headless']

  username = os.environ['GROUPME_USERNAME']
  password = os.environ['GROUPME_PASSWORD']

  if account == 'test':
    chat_labels = ['Chat Automation Testing']

  if account == 'southroads':
    chat_labels = ['Chat Southroads Leadership']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = groupme.routes.login_groupme(page, username, password)
    page = groupme.routes.message_groupme(page, chat_labels, groupme_message)
