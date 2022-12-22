from data.extract_catering_orders import extract_catering_orders
from data.pdf_to_text import pdf_to_text

def get_catering(options):
  
  files = options['files']
  results = {}

  for file in files.items():
    orders = extract_catering_orders(pdf_to_text(file[1]['path']))
    results[file[1]['label']] = orders

  return results