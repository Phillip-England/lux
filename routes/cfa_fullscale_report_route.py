import time

def cfa_fullscale_report_route(page):
  print('Attempting to go to CEM report builder..')
  page.goto('https://www.cfahome.com/go/appurl.go?app=SMGCLM')
  page.wait_for_selector('form[name="aspnetForm"]')
  page.goto('https://reporting.smg.com/ReportBuilder.aspx')
  page.wait_for_selector('select#rbReportTypeSEL')
  select = page.query_selector('select#rbReportTypeSEL')
  select.select_option("33")
  page.wait_for_selector('input#rbStartDateTB')
  page.click("div#measureDropDownContainer")
  scores = ["Overall Satisfaction", "Taste", "Attentive", "Cleanliness Combined", "Fast Service", "Order Accuracy"]
  for score in scores:
    page.keyboard.type(score)
    page.keyboard.press("Enter")
  print('CEM report builder loaded')
  return page
