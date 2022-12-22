from data.extract_cem_scores import extract_cem_scores
from data.pdf_to_text import pdf_to_text

def get_cems(options):

  files = options['files']
  results = {}
  
  for file in files.items():
    scores = extract_cem_scores(pdf_to_text(file[1]['path']))
    results[file[1]['label']] = scores

  return results