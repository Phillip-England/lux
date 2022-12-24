import os

from data.extract_catering_orders import extract_catering_orders
from data.pdf_to_text import pdf_to_text

def get_catering(options):
  
  files = options['files']
  results = {}

  for file in files:

    if file == 'tomorrow':
      label = 'tomorrow'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', 'southroads', 'catering', 'tomorrow.pdf')

    orders = extract_catering_orders(pdf_to_text(path))
    results[label] = orders

  return results