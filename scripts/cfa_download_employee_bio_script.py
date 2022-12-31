import os
import time

from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup

from routes import cfa_login_home_route
from routes import cfa_goto_hr_payroll_route
from routes import cfa_download_employee_bio_route

def cfa_download_employee_bio_script(options):

  headless = options['headless']
  account = options['account']

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
    page = cfa_goto_hr_payroll_route(page)
    page, employee_names = cfa_download_employee_bio_route(page)
    return employee_names