import os
import time

from playwright.sync_api import Playwright, sync_playwright

from util import format_date
from util import get_first_date_of_month
from util import get_last_date_of_month
from util import get_first_date_of_year
from util import get_last_date_of_year
from util import get_past_date
from util import last_day_of_prev_month
from util import first_day_of_prev_month

from routes import cfa_login_home_route
from routes import cfa_fullscale_report_route
from routes import cfa_download_cems_route

def cfa_download_cems_script(options):

  account = options['account']
  headless = options['headless']
  file_paths = options['file_paths']

  if 'date' in options:
    date = options['date']

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

    # RECENT DAY DOWNLOADS
    if 'recent_units_cem_path' in file_paths:
      print('hit')
      page = cfa_download_cems_route(page, format_date(get_past_date(4)), format_date(get_past_date(4)), "Units", file_paths['recent_units_cem_path'])
    if 'recent_time_of_day_cem_path' in file_paths:
      page = cfa_download_cems_route(page, format_date(get_past_date(4)), format_date(get_past_date(4)), "Time of Day", file_paths['recent_time_of_day_cem_path'])
    if 'recent_type_of_visit_cem_path' in file_paths:
      page = cfa_download_cems_route(page, format_date(get_past_date(4)), format_date(get_past_date(4)), "Type of Visit", file_paths['recent_type_of_visit_cem_path'])

    # CUSTOM DATE DOWNLOADS
    if 'custom_units_cem_path' in file_paths:
      page = cfa_download_cems_route(page, date, date, "Units", file_paths['custom_units_cem_path'])
    if 'custom_time_of_day_cem_path' in file_paths:
      page = cfa_download_cems_route(page, date, date, "Time of Day", file_paths['custom_time_of_day_cem_path'])
    if 'custom_type_of_visit_cem_path' in file_paths:
      page = cfa_download_cems_route(page, date, date, "Type of Visit", file_paths['custom_type_of_visit_cem_path'])
    
    # MONTH TO DATE DOWNLOAD
    if 'mtd_units_cem_path' in file_paths:
      page = cfa_download_cems_route(page, format_date(get_first_date_of_month()), format_date(get_last_date_of_month()), "Units", file_paths['mtd_units_cem_path'])
    
    # PREVIOUS MONTH DOWNLOAD
    if 'pm_units_cem_path' in file_paths:
      page = cfa_download_cems_route(page, format_date(first_day_of_prev_month()), format_date(last_day_of_prev_month()), "Units", file_paths['pm_units_cem_path'])
    
    # NINTY DAY ROLLING DOWNLOAD
    if 'ndr_units_cem_path' in file_paths:
      page = cfa_download_cems_route(page, format_date(get_past_date(90)), format_date(get_past_date(0)), "Units", file_paths['ndr_units_cem_path'])
    
    # YEAR TO DATE DOWNLOAD
    if 'ytd_units_cem_path' in file_paths:
      page = cfa_download_cems_route(page, format_date(get_first_date_of_year()), format_date(get_last_date_of_year()), "Units", file_paths['ytd_units_cem_path'])

    print("CEM HTML file downloaded")

    return page
