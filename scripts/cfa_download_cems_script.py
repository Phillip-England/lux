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

  if account == 'southroads':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']

  if account == 'test':
    username = os.environ['SOUTHROADS_USERNAME']
    password = os.environ['SOUTHROADS_PASSWORD']
  

  recent_units_cem_path = file_paths['recent_units_cem_path']
  recent_time_of_day_cem_path = file_paths['recent_time_of_day_cem_path']
  recent_type_of_visit_cem_path = file_paths['recent_type_of_visit_cem_path']
  mtd_units_cem_path = file_paths['mtd_units_cem_path']
  pm_units_cem_path = file_paths['pm_units_cem_path']
  ndr_units_cem_path = file_paths['ndr_units_cem_path']
  ytd_units_cem_path = file_paths['ytd_units_cem_path']


  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=headless)
    page = browser.new_page()
    page = cfa_login_home_route(page, username, password)
    page = cfa_fullscale_report_route(page)
    page = cfa_download_cems_route(page, format_date(get_past_date(4)), format_date(get_past_date(4)), "Units", recent_units_cem_path)
    page = cfa_download_cems_route(page, format_date(get_past_date(4)), format_date(get_past_date(4)), "Time of Day", recent_time_of_day_cem_path)
    page = cfa_download_cems_route(page, format_date(get_past_date(4)), format_date(get_past_date(4)), "Type of Visit", recent_type_of_visit_cem_path)
    page = cfa_download_cems_route(page, format_date(get_first_date_of_month()), format_date(get_last_date_of_month()), "Units", mtd_units_cem_path)
    page = cfa_download_cems_route(page, format_date(first_day_of_prev_month()), format_date(last_day_of_prev_month()), "Units", pm_units_cem_path)
    page = cfa_download_cems_route(page, format_date(get_past_date(90)), format_date(get_past_date(0)), "Units", ndr_units_cem_path)
    page = cfa_download_cems_route(page, format_date(get_first_date_of_year()), format_date(get_last_date_of_year()), "Units", ytd_units_cem_path)




    return page
