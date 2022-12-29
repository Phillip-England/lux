import os

def google_goto_cems_route(page):
  print('Attempting to load CEM tracking google form...')
  page.goto(os.environ['GOOGLE_CEM_TRACKING_FORM_URl'])
  page.wait_for_load_state('load')
  print('CEM tracking google form loaded')
  return page