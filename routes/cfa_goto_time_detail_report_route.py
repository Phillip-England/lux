def cfa_goto_time_detail_report_route(page):
  print('Attempting to goto time detail report page..')
  page.goto('https://backoffice.cfahome.com/tp/displayEmployeeTimeDetailInput.do')
  page.wait_for_load_state('load')
  print('Time detail report page loaded')
  return page