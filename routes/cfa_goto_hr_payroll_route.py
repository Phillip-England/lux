

def cfa_goto_hr_payroll_route(page):
  print("Attempting to go to HR payroll..")
  page.goto('https://www.cfahome.com/go/appurl.go?app=PAYROLL')
  page.wait_for_load_state('load')
  print('HR payroll loaded')
  return page