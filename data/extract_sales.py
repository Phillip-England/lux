from util import pdf_to_text
from util import contains_substring

def extract_sales(path):

  text = pdf_to_text(path)

  results = {

    'date': '',
    'day': '',

    'total_sales': '0',
    'breakfast_sales': '0',
    'lunch_sales': '0',
    'midshift_sales': '0',
    'dinner_sales': '0',
    'dine_in_sales': '0',
    'carryout_sales': '0',
    'drive_thru_sales': '0',
    'on_demand_sales': '0',
    'cfa_delivery_sales': '0',
    'm_dine_in_sales': '0',
    'm_carryout_sales': '0',
    'm_drive_thru_sales': '0',
    'curbside_sales': '0',
    'delivery_sales': '0',
    'pickup_sales': '0',

    'total_transactions': '0',
    'breakfast_transactions': '0',
    'lunch_transactions': '0',
    'midshift_transactions': '0',
    'dinner_transactions': '0',
    'dine_in_transactions': '0',
    'carryout_transactions': '0',
    'drive_thru_transactions': '0',
    'on_demand_transactions': '0',
    'cfa_delivery_transactions': '0',
    'm_dine_in_transactions': '0',
    'm_carryout_transactions': '0',
    'm_drive_thru_transactions': '0',
    'curbside_transactions': '0',
    'delivery_transactions': '0',
    'pickup_transactions': '0',

    'total_check_average': '0',
    'breakfast_check_average': '0',
    'lunch_check_average': '0',
    'midshift_check_average': '0',
    'dinner_check_average': '0',
    'dine_in_check_average': '0',
    'carryout_check_average': '0',
    'drive_thru_check_average': '0',
    'on_demand_check_average': '0',
    'cfa_delivery_check_average': '0',
    'm_dine_in_check_average': '0',
    'm_carryout_check_average': '0',
    'm_drive_thru_check_average': '0',
    'curbside_check_average': '0',
    'delivery_check_average': '0',
    'pickup_check_average': '0',


  }

  is_final_section = False
  destination_chunk_positions = []
  destination_names = ['CARRY OUT', 'CFA DELIVERY', 'CURBSIDE', 'DELIVERY', 'DINE IN', 'DRIVE THRU', 'M-CARRYOUT', 'M-DINEIN', 'M-DRIVE-THRU', 'ON DEMAND', 'PICK']

  for i in range(len(text)):
    
    # getting date and day
    if contains_substring(text[i], 'From'):
      subphrase = []
      words = text[i].split()
      for i in range(len(words)):
        if words[i] == 'From':
          results['day'] = words[i+1][:-1]
          month = words[i+2]
          day_of_month = words[i+3]
          year = words[i+4]
          results['date'] = f'{month} {day_of_month} {year}'
    
    # getting total sales
    if contains_substring(text[i], 'Report Totals:'):
      is_final_section = True
      results['total_transactions'] = text[i+1][:-1]
      results['total_sales'] = text[i+2][:-1]
      results['total_check_average'] = text[i+3][:-1]

    # scanning for destination details
    if is_final_section == True:
      

      # checking if any of our destination names exist in current chunk of data
      for destination in destination_names:
        # if we find the destination in
        if contains_substring(text[i], destination):
          if i not in destination_chunk_positions:
            destination_chunk_positions.append(i)
  
  print(destination_chunk_positions)
        







  return results