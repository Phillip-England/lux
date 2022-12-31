import os

def google_goto_sales_form_route(page, url):
  print('Attempting to load google sales tracking form..')
  page.goto(url)
  page.wait_for_load_state('load')
  print('Google sales tracking form loaded')
  return page