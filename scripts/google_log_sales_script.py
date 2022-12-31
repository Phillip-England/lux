import os

from playwright.sync_api import Playwright, sync_playwright

from routes import google_goto_sales_form_route
from routes import google_submit_sales_tracking_form_route

def google_log_sales_script(options):

  data = options['data']
  headless = options['headless']
  account = options['account']

  if account == 'test':
    google_form_url = os.environ['GOOGLE_SOUTHROADS_SALES_TRACKING_FORM_URL']

  if account == 'southroads':
    google_form_url = os.environ['GOOGLE_SOUTHROADS_SALES_TRACKING_FORM_URL']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = google_goto_sales_form_route(page, google_form_url)
    page = google_submit_sales_tracking_form_route(page, data)