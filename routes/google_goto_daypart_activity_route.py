import os

def google_goto_daypart_activity_route(page):
  print('Attempting to load google sales tracking form..')
  page.goto(os.environ['GOOGLE_SALES_TRACKING_FORM_URL'])
  page.wait_for_load_state('load')
  print('Google sales tracking form loaded')
  return page