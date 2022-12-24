import os

from playwright.sync_api import Playwright, sync_playwright
from routes.slack.login import login
from routes.slack.message import message

def slack_message(options):

  account = options['account']
  message_list = options['message_list']
  headless = options['headless']

  if account == 'test': 
    login_url = 'https://testing-hkz9125.slack.com/sign_in_with_password'
    username = os.environ['SLACK_USERNAME']
    password = os.environ['SLACK_PASSWORD']
    channel_ids = ('C04EAJBBT4G', 'C04DZGFD9A5', 'C04EAJB016C')
  
  if account == 'southroads': 
    login_url = 'https://cfasouthroads.slack.com/sign_in_with_password'
    username = os.environ['SLACK_USERNAME']
    password = os.environ['SLACK_PASSWORD']
    channel_ids = ('C02AG6SCFDY')

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = login(page, login_url, username, password)
    page = message(page, message_list, channel_ids)