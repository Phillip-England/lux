def cfa_download_daypart_activity_route(page, start, end, save_as):
  print(f'Attempting to download daypart activity report for {start}-{end}..')
  start_date_input = page.query_selector('input#MainContent_BusDate1_I')
  end_date_input = page.query_selector('input#MainContent_BusDate2_I')
  start_date_input.fill('')
  start_date_input.type(start)
  end_date_input.fill('')
  end_date_input.type(end)
  try:
    with page.expect_download() as download_info:
      page.click('input#MainContent_btnGenerateButton')
      download = download_info.value
      download.save_as(f'{save_as}')
      print(f'Daypart activity downloaded for {start}-{end}')
  except:
    print(f"No daypart activity report for {start}-{end}")
  return page
