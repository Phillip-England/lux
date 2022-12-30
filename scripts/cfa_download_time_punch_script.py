import os
import time

from playwright.sync_api import Playwright, sync_playwright

from util import format_date
from util import get_past_date

from routes import cfa_login_home_route
from routes import cfa_goto_time_detail_report_route
from routes import cfa_download_time_detail_report_route

def cfa_download_time_punch_script(options):

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
    context = browser.new_context()
    page = context.new_page()
    page.expect_popup
    page = cfa_login_home_route(page, username, password)
    page = cfa_goto_time_detail_report_route(page)
    page = cfa_download_time_detail_report_route(page, context, options={
      'start_date': format_date(get_past_date(30)),
      'end_date': format_date(get_past_date(0)),
      'save_as': os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'time-punch', 'punch.pdf')
    })
    # time.sleep(20)
  