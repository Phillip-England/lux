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

    for date in dates:
      if date == 'ytd':
        start = format_date(get_first_date_of_year())
        end = format_date(get_last_date_of_year())
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'ytd.pdf')
      if date == 'ndr':
        start = format_date(get_past_date(90))
        end = format_date(get_past_date(0))
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'ndr.pdf')
      if date == 'mtd':
        start = format_date(get_first_date_of_month())
        end = format_date(get_last_date_of_month())
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'mtd.pdf')
      if date == 'recent':
        start = format_date(get_past_date(3))
        end = format_date(get_past_date(3))
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'recent.pdf')
      page = cfa_download_cems_route(page, start, end, path)
    return page
