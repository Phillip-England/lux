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
  headless = options['headless']
  start_date = options['start_date']
  end_date = options['end_date']
  download_path = options['download_path']

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

    try:
      print(f'Attempting to delete: {download_path}')
      os.remove(download_path)
      print(f'Deleted: {download_path}')
    except:
      print(f'Does not exist to be deleted: {download_path}')

    page = cfa_download_daypart_activity_route(page, start_date, end_date, download_path)

    if os.path.exists(download_path):
      return True
    else:
      return False
  

    

