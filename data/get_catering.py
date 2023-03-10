import os

from data import extract_catering_orders
from util import pdf_to_text

def get_catering(options):
  
  files = options['files']
  account = options['account']
  results = {}

  for file in files:

    if file == 'tomorrow':
      label = 'tomorrow'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'catering', 'tomorrow.pdf')
      orders = extract_catering_orders(pdf_to_text(path))
      results[label] = orders

  return results