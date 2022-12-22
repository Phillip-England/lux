from playwright.sync_api import Playwright, sync_playwright
import os
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

  username = options['username']
  password = options['password']
  dates = options['dates']

  with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page = login(page, username, password)
    page = cem_full_scale_report(page)
    for timeframe in dates.items():
      start = timeframe[1]['start']
      end = timeframe[1]['end']
      path = timeframe[1]['path']
      page = cem_download_report(page, start, end, path)
    return page
