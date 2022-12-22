from playwright.sync_api import Playwright, sync_playwright
from routes.slack.login import login

def slack_message(options):

  username = options['username']
  password = options['password']
  workspace_url = options['workspace_url']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page = login(page, workspace_url, username, password)