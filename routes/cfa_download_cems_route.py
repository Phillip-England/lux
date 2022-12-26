import time

# This function has no problem pulling in a date without any data. You can do whatever date you'd like.

def cfa_download_cems_route(page, start_date, end_date, save_as):
  print(f'Attemping to download cem report for date range {start_date}-{end_date}')
  start_date_input = page.query_selector('input#rbStartDateTB')
  start_date_input.fill('')
  start_date_input.type(start_date)
  end_date_input = page.query_selector('input#rbEndDateTB')
  end_date_input.fill('')
  end_date_input.type(end_date)
  page.click('span#rbSurveyItemSelectAllLBL')
  page.click('div#rbBuildReportBTN')
  page.wait_for_selector('div.textAfter')
  page.click('div.textAfter')
  page.wait_for_selector('label#rvsPDFLBL')
  page.click('label#rvsPDFLBL')
  with page.expect_download() as download_info:
    page.click('div#rvsDownloadBTN')
    download = download_info.value
    download.save_as(f'{save_as}')
  print(f'CEM report for {start_date}-{end_date} downloaded')
  return page