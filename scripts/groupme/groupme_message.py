from playwright.sync_api import Playwright, sync_playwright
from routes.groupme.login import login
from routes.groupme.message import message
import os

def groupme_message(options):

  account = options['account']
  groupme_message = options['message']
  headless = options['headless']

  if account == 'test':
    username = os.environ['GROUPME_TESTING_USERNAME']
    password = os.environ['GROUPME_TESTING_PASSWORD']
    chat_labels = ['Chat testing', 'Chat testing 2'],

  if account == 'southroads':
    username = os.environ['GROUPME_TESTING_USERNAME']
    password = os.environ['GROUPME_TESTING_PASSWORD']
    chat_labels = 'Chat testing',

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = login(page, username, password)
    page = message(page, chat_labels, groupme_message)
