import os

from playwright.sync_api import Playwright, sync_playwright
from routes.cfa.login import login
from routes.cfa.cem_full_scale_report import cem_full_scale_report
from routes.cfa.cem_download_report import cem_download_report
from date.format_date import format_date
from date.get_first_date_of_month import get_first_date_of_month
from date.get_last_date_of_month import get_last_date_of_month
from date.get_first_date_of_year import get_first_date_of_year
from date.get_last_date_of_year import get_last_date_of_year
from date.get_past_date import get_past_date

def download_cems(options):

  dates = options['dates']
  account = options['account']
  headless = options['headless']

  if account == 'southroads':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = login(page, username, password)
    page = cem_full_scale_report(page)

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
      page = cem_download_report(page, start, end, path)
    return page
