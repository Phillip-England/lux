from playwright.sync_api import Playwright, sync_playwright

from routes import google_goto_cems_route
from routes import google_submit_cems_form_route

def google_log_cems_script(options):

  data = options['data']
  headless = options['headless']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = google_goto_cems_route(page)
    page = google_submit_cems_form_route(page, data)
  

