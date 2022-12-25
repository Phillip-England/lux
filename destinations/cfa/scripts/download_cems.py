import os

from playwright.sync_api import Playwright, sync_playwright
from destinations import cfa
from util import format_date
from util import get_first_date_of_month
from util import get_last_date_of_month
from util import get_first_date_of_year
from util import get_last_date_of_year
from util import get_past_date

def download_cems(options):

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
    page = cfa.routes.login_cfahome(page, username, password)
    page = cfa.routes.goto_cem_fullscale_report(page)

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
      page = cfa.routes.download_cems(page, start, end, path)
    return page
