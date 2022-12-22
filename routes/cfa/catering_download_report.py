import time

def catering_download_report(page, start_date, end_date, save_as):
  print(f'Attempting to download catering report for {start_date}-{end_date}..')
  page.goto('https://rsmw.cfahome.com/SMW18-00/StoreMgmtKOReportDeferredOrderCFA.aspx')
  page.wait_for_selector('input#MainContent_BusDate1_I')
  start_date_input = page.query_selector('input#MainContent_BusDate1_I')
  start_date_input.fill('')
  start_date_input.type(start_date)
  end_date_input = page.query_selector('input#MainContent_BusDate2_I')
  end_date_input.fill('')
  end_date_input.type(end_date)
  with page.expect_download() as download_info:
    page.click('input#MainContent_btnGenerateButton')
    download = download_info.value
    download.save_as(f'{save_as}')
  time.sleep(5)
  print(f'Catering report for {start_date}-{end_date} downloaded')
  return page

  