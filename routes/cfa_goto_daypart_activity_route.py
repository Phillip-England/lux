def cfa_goto_daypart_activity_route(page):
  print("Attempting to go to daypart activity report download page..")
  page.goto('https://rsmw.cfahome.com/SMW18-00/StoreMgmtKOReportDayPart.aspx')
  page.wait_for_selector('div#btnMakeFavorite_CD')
  print('Daypart activity report page loaded')
  return page