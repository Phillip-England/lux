import os

def google_goto_cems_form_route(page, url):
  print('Attempting to load CEM tracking google form...')
  page.goto(url)
  page.wait_for_load_state('load')
  print('CEM tracking google form loaded')
  return page