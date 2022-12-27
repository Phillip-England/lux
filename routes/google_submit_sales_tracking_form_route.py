import time

def google_submit_sales_tracking_form_route(page, sales_data):

  print('Attempting to log sales data..')

  page.click('input[jsname="YPqjbf"]')

  for datapoint in sales_data.values():
    page.keyboard.type(datapoint)
    page.keyboard.press('Tab')
  
  page.keyboard.press('Enter')
  page.wait_for_selector('div.c2gzEf')
  print('Sales data successfully logged')
    

