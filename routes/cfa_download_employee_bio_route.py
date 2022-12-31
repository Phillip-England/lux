import time
from bs4 import BeautifulSoup

def cfa_download_employee_bio_route(page):
  print('Attempting to load employee reports..')
  page.click('a#allreports')
  page.wait_for_selector('a#employeebio')
  print('Employee reports loaded')
  print('Attempting to download employee bio..')
  page.click('a#employeebio')
  page.wait_for_load_state('load')
  time.sleep(2)
  print('Extracting employee names from html')
  soup = BeautifulSoup(page.content(), 'html.parser')
  employee_a_tags = soup.find_all('a', class_='enabledLink')
  employee_names = []
  for tag in employee_a_tags:
    employee_names.append(tag.text)
  if len(employee_names) == 0:
    raise 'Failed to downloaded employees from employee bio'
  print('Employee bio downloaded')
  return (page, employee_names)