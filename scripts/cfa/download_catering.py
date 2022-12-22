from playwright.sync_api import Playwright, sync_playwright
from routes.cfa.login import login
from date.get_future_date import get_future_date
from date.format_date import format_date
from routes.cfa.login_service_point import login_service_point
from routes.cfa.catering_download_report import catering_download_report

def download_catering(options):

  username = options['username']
  password = options['password']
  pin = options['servicepoint_pin']
  dates = options['dates']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page = login(page, username, password)
    page = login_service_point(page, pin)

    for timeframe in dates.items():
      start = timeframe[1]['start']
      end = timeframe[1]['end']
      path = timeframe[1]['path']
      page = catering_download_report(page, start, end, path)

  return page
