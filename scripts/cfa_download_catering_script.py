import os

from playwright.sync_api import Playwright, sync_playwright

from routes import cfa_login_home_route
from routes import cfa_login_servicepoint_route
from routes import cfa_download_catering_route
from util import get_future_date
from util import format_date


def cfa_download_catering_script(options):

  account = options['account']
  dates = options['dates']
  headless = options['headless']

  if account == 'southroads':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']
    servicepoint_pin = os.environ['SOUTHROADS_SERVICEPOINT_PIN']
    os

  if account == 'test':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']
    servicepoint_pin = os.environ['SOUTHROADS_SERVICEPOINT_PIN']
    os

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = cfa_login_home_route(page, username, password)
    page = cfa_login_servicepoint_route(page, servicepoint_pin)

    paths = []

    for date in dates:

      if date == 'tomorrow':  
        start = format_date(get_future_date(1))
        end = format_date(get_future_date(1))
        path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'catering', 'tomorrow.pdf')
        paths.append(path)
        try:
          print(f"Attempting to delete: {path}")
          os.remove(path)
          print (f'Deleted file: {path}')
        except:
          print(f"Catering file does not exist at {path}")
        page = cfa_download_catering_route(page, start, end, path)

      # enter future dates here if you decide to grab the next 3 days catering and display

    for path in paths:
      if os.path.exists(path) == False:
        paths.remove(path)

  return paths
