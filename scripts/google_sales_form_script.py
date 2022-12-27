
from playwright.sync_api import Playwright, sync_playwright

from routes import google_goto_sales_tracking_form_route
from routes import google_submit_sales_tracking_form_route

def google_sales_form_script(options):

  data = options['data']
  headless = options['headless']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = google_goto_sales_tracking_form_route(page)
    page = google_submit_sales_tracking_form_route(page, data)