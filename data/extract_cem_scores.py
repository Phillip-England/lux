def extract_cem_scores(pdf_data):

  results = {
    'surveys': '0',
    'osat': 'N/A',
    'taste': 'N/A',
    'speed': 'N/A',
    'ace': 'N/A',
    'clean': 'N/A',
    'accuracy': 'N/A',
  }

  # indicators
  speed_indicator = 'Service'
  speed_steps = 10
  ace_indicator = 'Attentive/Courteous'
  ace_steps = 10
  clean_indicator = 'Combined'
  clean_steps = 10
  accuracy_indicator = 'Accuracy'
  accuracy_steps = 9

  for i in range(len(pdf_data)):


    if pdf_data[i] == 'Satisfaction':
      results['osat'] = pdf_data[i+10]

    if pdf_data[i] == 'Taste':
      if pdf_data[i+1] == '03253':
        results['taste'] = pdf_data[i+10]
        results['surveys'] = pdf_data[i-2]

    if pdf_data[i] == 'Service':
      results['speed'] = pdf_data[i+10]

    if pdf_data[i] == 'Attentive/Courteous':
      results['ace'] = pdf_data[i+10]

    if pdf_data[i] == 'Combined':
      results['clean'] = pdf_data[i+10]

    if pdf_data[i] == 'Accuracy':
      results['accuracy'] = pdf_data[i+9]

  # if not reponses have been submitted, we need to set values to N/A
  # response destination with no surveys will end up having a value of 'Responses'
  # this can occur at the very start of the month

  if results['osat'] == 'Responses': results['osat'] = 'N/A'
  if results['taste'] == 'Responses': results['taste'] = 'N/A'
  if results['speed'] == 'Responses': results['speed'] = 'N/A'
  if results['ace'] == 'Responses': results['ace'] = 'N/A'
  if results['clean'] == 'Responses': results['clean'] = 'N/A'
  if results['accuracy'] == 'Responses': results['accuracy'] = 'N/A'


  return results