import os

from playwright.sync_api import Playwright, sync_playwright

from util import format_date
from util import get_first_date_of_month
from util import get_last_date_of_month
from util import get_first_date_of_year
from util import get_last_date_of_year
from util import get_past_date
from routes import cfa_login_home_route
from routes import cfa_fullscale_report_route
from routes import cfa_download_cems_route

def cfa_download_cems_script(options):

  dates = options['dates']
  account = options['account']
  headless = options['headless']

  if account == 'southroads':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']

  if account == 'test':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = cfa_login_home_route(page, username, password)
    page = cfa_fullscale_report_route(page)

    for timeframe in dates.values():
      path = timeframe['path']
      start_date = timeframe['start_date']
      end_date = timeframe['end_date']
      try:
        print(f"Attempting to delete file: {path}")
        os.remove(path)
        print(f'File deleted: {path}')
      except:
        print(f'File does not exist to be deleted: {path}')
      page = cfa_download_cems_route(page, start_date, end_date, path)

    return page
