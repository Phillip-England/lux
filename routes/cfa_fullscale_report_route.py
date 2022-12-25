def cfa_fullscale_report_route(page):
  print('Attemping to go to CEM report builder')
  page.goto('https://www.cfahome.com/go/appurl.go?app=SMGCLM')
  page.wait_for_selector('form[name="aspnetForm"]')
  page.goto('https://reporting.smg.com/ReportBuilder.aspx')
  page.wait_for_selector('select#rbReportTypeSEL')
  select = page.query_selector('select#rbReportTypeSEL')
  select.select_option("33")
  page.wait_for_selector('input#rbStartDateTB')
  print('CEM report builder loaded')
  return page
