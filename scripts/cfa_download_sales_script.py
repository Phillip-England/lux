import os

from playwright.sync_api import Playwright, sync_playwright

from routes import cfa_login_home_route
from routes import cfa_login_servicepoint_route
from routes import cfa_goto_daypart_activity_route
from routes import cfa_download_daypart_activity_route

from util import format_date
from util import get_past_date
from util import get_first_date_of_month
from util import get_last_date_of_month
from util import get_first_date_of_year
from util import get_last_date_of_year


def cfa_download_sales_script(options):
  
  account = options['account']
  dates = options['dates']
  headless = options['headless']

  if account == 'southroads':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']
    pin = os.environ['SOUTHROADS_SERVICEPOINT_PIN']

  if account == 'test':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']
    pin = os.environ['SOUTHROADS_SERVICEPOINT_PIN']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = cfa_login_home_route(page, username, password)
    page = cfa_login_servicepoint_route(page, pin)
    page = cfa_goto_daypart_activity_route(page)

    paths = []

    for date in dates:

      if date == 'yesterday':
        start = format_date(get_past_date(1))
        end = format_date(get_past_date(1))
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'yesterday.pdf')
        paths.append(path)
        try:
          print(f"Attempting to delete: {path}")
          os.remove(os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'yesterday.pdf'))
          print(f"Deleted: {path}")
        except:
          print(f"Does not exist to be deleted: {path}")
        page = cfa_download_daypart_activity_route(page, start, end, path)

      if date == 'mtd':
        start = format_date(get_first_date_of_month())
        end = format_date(get_last_date_of_month())
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'mtd.pdf')
        paths.append(path)
        try:
          print(f"Attempting to delete: {path}")
          os.remove(os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'mtd.pdf'))
          print(f"Deleted: {path}")
        except:
          print(f"Does not exist to be deleted: {path}")
        page = cfa_download_daypart_activity_route(page, start, end, path)

      if date == 'ytd':
        start = format_date(get_first_date_of_year())
        end = format_date(get_last_date_of_year())
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'ytd.pdf')
        paths.append(path)
        try:
          print(f"Attempting to delete: {path}")
          os.remove(os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'ytd.pdf'))
          print(f"Deleted: {path}")
        except:
          print(f"Does not exist to be deleted: {path}")
        page = cfa_download_daypart_activity_route(page, start, end, path)

      
    for path in paths:
      if os.path.exists(path) == False:
        paths.remove(path)

    return paths

    

