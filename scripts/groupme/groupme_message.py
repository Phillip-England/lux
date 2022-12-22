from playwright.sync_api import Playwright, sync_playwright
from routes.groupme.login import login
from routes.groupme.message import message

def groupme_message(options):

  username = options['username']
  password = options['password']
  chat_label = options['chat_label']
  groupme_message = options['message']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page = login(page, username, password, chat_label)
    page = message(page, chat_label, groupme_message)
