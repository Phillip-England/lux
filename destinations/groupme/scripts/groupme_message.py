from playwright.sync_api import Playwright, sync_playwright
from destinations import groupme
import os

def groupme_message(options):

  account = options['account']
  groupme_message = options['message']
  headless = options['headless']

  if account == 'test':
    username = os.environ['GROUPME_TESTING_USERNAME']
    password = os.environ['GROUPME_TESTING_PASSWORD']
    chat_labels = ('Chat testing', 'Chat testing 2')

  if account == 'southroads':
    username = os.environ['GROUPME_TESTING_USERNAME']
    password = os.environ['GROUPME_TESTING_PASSWORD']
    chat_labels = 'Chat testing'

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = groupme.routes.login_groupme(page, username, password)
    page = groupme.routes.message_groupme(page, chat_labels, groupme_message)
