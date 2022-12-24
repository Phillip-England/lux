def extract_cem_scores(pdf_data):

  results = {
    'osat': '',
    'taste': '',
    'speed': '',
    'ace': '',
    'clean': '',
    'accuracy': '',
    'surveys': ''
  }

  # indicators
  osat_indicator = 'Satisfaction'
  osat_steps = 10
  taste_indicator = 'Taste'
  taste_steps = 10
  speed_indicator = 'Service'
  speed_steps = 10
  ace_indicator = 'Attentive/Courteous'
  ace_steps = 10
  clean_indicator = 'Combined'
  clean_steps = 10
  accuracy_indicator = 'Accuracy'
  accuracy_steps = 9

  for i in range(len(pdf_data)):

    if pdf_data[i] == osat_indicator:
      results['osat'] = pdf_data[i+osat_steps]

    if pdf_data[i] == taste_indicator:
      if pdf_data[i+1] == '03253':
        results['taste'] = pdf_data[i+taste_steps]
        results['surveys'] = pdf_data[i-2]

    if pdf_data[i] == speed_indicator:
      results['speed'] = pdf_data[i+speed_steps]

    if pdf_data[i] == ace_indicator:
      results['ace'] = pdf_data[i+ace_steps]

    if pdf_data[i] == clean_indicator:
      results['clean'] = pdf_data[i+clean_steps]

    if pdf_data[i] == accuracy_indicator:
      results['accuracy'] = pdf_data[i+accuracy_steps]

  return results