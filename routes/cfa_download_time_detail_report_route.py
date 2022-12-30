import time
import pyautogui
import os

def cfa_download_time_detail_report_route(page, context, options):

  start_date = options['start_date']
  end_date = options['end_date']
  save_as = options['save_as']

  print(f'Attempting to download time detail report for {start_date}-{end_date}..')
  start_date_input = page.query_selector('input#reportStartDate')
  end_date_input = page.query_selector('input#reportEndDate')
  start_date_input.fill('')
  end_date_input.fill('')
  start_date_input.type(start_date)
  end_date_input.type(end_date)
  page.click('input[value="View Report"]')
  print('Time punch report pdf page loading..')
  time.sleep(30)
  page.bring_to_front()
  pdf_page = context.pages[1]
  pdf_page.bring_to_front()
  time.sleep(5)
  with pdf_page.expect_download() as download_info:
    download_button_location = pyautogui.locateOnScreen(os.path.join(os.environ['PROJECT_PATH'], 'images', 'download_icon.png'))
    x, y = pyautogui.center(download_button_location)
    pyautogui.click(x, y)
    download = download_info.value
    download.save_as(save_as)
  print(f'Time detail report downloaded for {start_date}-{end_date}')

  