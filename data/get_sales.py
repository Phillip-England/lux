import os

from util import pdf_to_text
from data import extract_sales

def get_sales(options):

  files = options['files']
  account = options['account']
  results = {}

  for file in files:

    if file == 'yesterday':
      label = 'yesterday'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'yesterday.pdf')
      sales = extract_sales(pdf_to_text(path))
      results[label] = sales

  return results