from pdfminer.high_level import extract_text
from util import pdf_to_text


def extract_daypart_activity(path):

  text = pdf_to_text(path)

  results = {

    'date': '',
    'day': '',

    'total_sales': '0',
    'breakfast_sales': '0',
    'lunch_sales': '0',
    'midshift_sales': '0',
    'dinner_sales': '0',

    'total_transactions': '0',
    'breakfast_transactions': '0',
    'lunch_transactions': '0',
    'midshift_transactions': '0',
    'dinner_transactions': '0',

    'total_check_average': '0',
    'breakfast_check_average': '0',
    'lunch_check_average': '0',
    'midshift_check_average': '0',
    'dinner_check_average': '0',
   
  }

  for i in range(len(text)):

    if text[i] == 'Time:From':
      results['day'] = text[i+1][:-1]
      month = text[i+2]
      day_of_month = text[i+3]
      year = text[i+4]
      results['date'] = f'{month} {day_of_month} {year}'

    if text[i] == 'Breakfast':
      results['breakfast_transactions'] = text[i+3].strip('Daypart/DestinationTransaction')
      results['breakfast_sales'] = text[i+4].strip('Daypart/DestinationTransaction')
      results['breakfast_check_average'] = text[i+5].strip('Daypart/DestinationTransaction')

    if text[i] == 'Lunch':
      results['lunch_transactions'] = text[i+3].strip('Daypart/DestinationTransaction')
      results['lunch_sales'] = text[i+4].strip('Daypart/DestinationTransaction')
      results['lunch_check_average'] = text[i+5].strip('Daypart/DestinationTransaction')

    if text[i] == 'Afternoon':
      results['midshift_transactions'] = text[i+3].strip('Daypart/DestinationTransaction')
      results['midshift_sales'] = text[i+4].strip('Daypart/DestinationTransaction')
      results['midshift_check_average'] = text[i+5].strip('Daypart/DestinationTransaction')

    if text[i] == 'Dinner':
      results['dinner_transactions'] = text[i+3].strip('Daypart/DestinationTransaction')
      results['dinner_sales'] = text[i+4].strip('Daypart/DestinationTransaction')
      results['dinner_check_average'] = text[i+5].strip('Daypart/DestinationTransaction')


    if text[i] == 'Totals:':
      results['total_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
      results['total_sales'] = text[i+2].strip('Daypart/DestinationTransaction')
      results['total_check_average'] = text[i+3].strip('Daypart/DestinationTransaction')


  
  return results




  