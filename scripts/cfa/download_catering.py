import os

from playwright.sync_api import Playwright, sync_playwright
from routes.cfa.login import login
from date.get_future_date import get_future_date
from date.format_date import format_date
from routes.cfa.login_service_point import login_service_point
from routes.cfa.catering_download_report import catering_download_report

def download_catering(options):

  account = options['account']
  dates = options['dates']
  headless = options['headless']

  if account == 'southroads':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']
    servicepoint_pin = os.environ['SOUTHROADS_SERVICEPOINT_PIN']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = login(page, username, password)
    page = login_service_point(page, servicepoint_pin)

    for date in dates:

      if date == 'tomorrow':  
        start = format_date(get_future_date(1))
        end = format_date(get_future_date(1))
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'catering', 'tomorrow.pdf')
      page = catering_download_report(page, start, end, path)

  return page
