import os
import time

from bs4 import BeautifulSoup

from util import get_date_object
from util import get_day_of_week

def cfa_download_cems_route(page, start_date, end_date, breakout, save_as):

  print(f'Attemping to download cem report for date range {start_date}-{end_date} with breakout {breakout}')
  
  try:
    print(f"Attempting to delete: {save_as}")
    os.remove(save_as)
    print(f"Deleted file: {save_as}")
  except:
    print(f"No file exists to delete at: {save_as}")

  start_date_input = page.query_selector('input#rbStartDateTB')
  start_date_input.fill('')
  start_date_input.type(start_date)
  end_date_input = page.query_selector('input#rbEndDateTB')
  end_date_input.fill('')
  end_date_input.type(end_date)
  page.click("div.reversePodButton")
  page.click("div#rbCompareByUnits")
  page.keyboard.type(breakout)
  page.keyboard.press('Enter')
  page.click("div#rbDoneBTN")
  page.click('div#rbBuildReportBTN')
  page.wait_for_selector(f"div#rvTitleDiv")

  content = page.content()

  # checking if data exists for the given day
  soup = BeautifulSoup(content, 'html.parser')
  error_element = soup.find("td", {"class": "Default_Error_Text"})

  # logging if we have an error
  file =  open(save_as, "a")
  if error_element != None:
    file.write(f"<div id=__error_exists>TRUE</div>\n")
  else:
    file.write(f"<div id=__error_exists>FALSE</div>\n")
  
  file.write(f"<div id=__start_date>{start_date}</div>\n")
  file.write(f"<div id=__end_date>{end_date}</div>\n")
  file.write(f"<div id=__start_day_of_week>{get_day_of_week(get_date_object(start_date))}</div>\n")
  file.write(f"<div id=__end_day_of_week>{get_day_of_week(get_date_object(end_date))}</div>\n")
  file.write('\n')
  file.write(content)
  file.close()
  return page
