def cfa_goto_daypart_activity_route(page, pin):
  print("Attempting to go to daypart activity report download page..")
  page.goto('https://rsmw.cfahome.com/SMW18-00/StoreMgmtKOReportDayPart.aspx')
  page.wait_for_selector('input#MainContent_txtEchoWindow')
  page.type('input#MainContent_txtEchoWindow', pin)
  page.click('input#MainContent_btnEnter')
  page.wait_for_selector('div#btnMakeFavorite')
  page.wait_for_selector('div#btnMakeFavorite_CD')
  page.goto('https://rsmw.cfahome.com/SMW18-00/StoreMgmtKOReportDayPart.aspx')
  print('Daypart activity report page loaded')
  return page