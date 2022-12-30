from pdfminer.high_level import extract_text
from util import pdf_to_text
from util import contains_substring


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
    'carryout_sales': '0',
    'cfa_delivery_sales': '0',
    'delivery_sales': '0',
    'dine_in_sales': '0',
    'drive_thru_sales': '0',
    'm_carry_out_sales': '0',
    'm_dine_in_sales': '0',
    'm_drive_thru_sales': '0',
    'on_demand_sales': '0',
    'pickup_sales': '0',
    'curbside_sales': '0',

    'total_transactions': '0',
    'breakfast_transactions': '0',
    'lunch_transactions': '0',
    'midshift_transactions': '0',
    'dinner_transactions': '0',
    'carryout_transactions': '0',
    'cfa_delivery_transactions': '0',
    'delivery_transactions': '0',
    'dine_in_transactions': '0',
    'drive_thru_transactions': '0',
    'm_carry_out_transactions': '0',
    'm_dine_in_transactions': '0',
    'm_drive_thru_transactions': '0',
    'on_demand_transactions': '0',
    'pickup_transactions': '0',
    'curbside_transactions': '0',

    'total_check_average': '0',
    'breakfast_check_average': '0',
    'lunch_check_average': '0',
    'midshift_check_average': '0',
    'dinner_check_average': '0',
    'carryout_check_average': '0',
    'cfa_delivery_check_average': '0',
    'delivery_check_average': '0',
    'dine_in_check_average': '0',
    'drive_thru_check_average': '0',
    'm_carry_out_check_average': '0',
    'm_dine_in_check_average': '0',
    'm_drive_thru_check_average': '0',
    'on_demand_check_average': '0',
    'pickup_check_average': '0',
    'curbside_check_average': '0',

  }

  is_final_section = False

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
      is_final_section = True
      results['total_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
      results['total_sales'] = text[i+2].strip('Daypart/DestinationTransaction')
      results['total_check_average'] = text[i+3].strip('Daypart/DestinationTransaction')


    if is_final_section:

      if contains_substring(text[i], 'OUT') and contains_substring(text[i-1], 'CARRY'):
        results['carryout_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['carryout_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['carryout_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if text[i] == 'DELIVERY' and contains_substring(text[i-1], 'CFA'):
        results['cfa_delivery_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['cfa_delivery_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['cfa_delivery_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'DELIVERY') and not contains_substring(text[i-1], 'CFA'):
        results['delivery_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['delivery_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['delivery_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'IN') and contains_substring(text[i-1], 'DINE'):
        results['dine_in_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['dine_in_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['dine_in_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'THRU') and contains_substring(text[i-1], 'DRIVE'):
        results['drive_thru_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['drive_thru_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['drive_thru_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'M-CARRYOUT'):
        results['m_carry_out_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['m_carry_out_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['m_carry_out_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'M-DINEIN'):
        results['m_dine_in_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['m_dine_in_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['m_dine_in_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'M-DRIVE-THRU'):
        results['m_drive_thru_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['m_drive_thru_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['m_drive_thru_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'DEMAND') and contains_substring(text[i-1], 'ON'):
        results['on_demand_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['on_demand_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['on_demand_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'PICKUP'):
        results['pickup_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['pickup_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['pickup_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

      if contains_substring(text[i], 'CURBSIDE'):
        results['curbside_transactions'] = text[i+1].strip('Daypart/DestinationTransaction')
        results['curbside_sales'] = text[i+3].strip('Daypart/DestinationTransaction')
        results['curbside_check_average'] = text[i+2].strip('Daypart/DestinationTransaction')

  
  return results




  