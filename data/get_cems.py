import os

from data.extract_cem_scores import extract_cem_scores
from data.pdf_to_text import pdf_to_text

def get_cems(options):

  files = options['files']
  account = options['account']
  results = {}

  for file in files:

    if file == 'ytd':
      label = 'ytd'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'ytd.pdf')

    if file == 'ndr':
      label = 'ndr'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'ndr.pdf')

    if file == 'mtd':
      label = 'mtd'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'mtd.pdf')

    if file == 'recent':
      label = 'recent'
      path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'recent.pdf')
  
    scores = extract_cem_scores(pdf_to_text(path))
    results[label] = scores

  return results