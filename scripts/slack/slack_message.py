from playwright.sync_api import Playwright, sync_playwright
from routes.slack.login import login

def slack_message(options):

  username = options['username']
  password = options['password']
  account = options['account']

  if account == 'test': login_url = 'https://testing-hkz9125.slack.com/sign_in_with_password'
  if account == 'southroads': login_url = 'https://cfasouthroads.slack.com/sign_in_with_password'

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page = login(page, login_url, username, password)