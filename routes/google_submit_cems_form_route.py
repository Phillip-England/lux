import time

def google_submit_cems_form_route(page, data):

  print('Attempting to log cem data..')

  page.click('input[jsname="YPqjbf"]')

  for datapoint in data.values():
    page.keyboard.type(datapoint)
    page.keyboard.press('Tab')
  
  page.keyboard.press('Enter')
  time.sleep(2)
  page.wait_for_selector('div.c2gzEf')
  
  return page