import re

from pdfminer.high_level import extract_pages, extract_text


from util import pdf_to_text
from util import contains_substring

def extract_sales(path):

  text = extract_text(path).split()

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

  # looping variables
  is_final_section = False
  carryout_sales = []
  carryout_transactions = []
  carryout_check_averages = []
  cfa_delivery_sales = []
  cfa_delivery_transactions = []
  cfa_delivery_check_averages = []

  for i in range(len(text)):

    # settings up final section trigger
    if text[i] == 'Totals:':
      is_final_section = True

    if text[i] == 'CARRY' and text[i+1] == 'OUT' and is_final_section == False:
      carryout_transactions.append(text[i+2])
      carryout_sales.append(text[i+3])
      carryout_check_averages.append(text[i+4])

    if text[i] == 'CFA' and text[i+1] == 'DELIVERY' and is_final_section == False:
      cfa_delivery_transactions.append(text[i+2])
      cfa_delivery_sales.append(text[i+3])
      cfa_delivery_check_averages.append(text[i+4])

  