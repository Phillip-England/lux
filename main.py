import os
import sys

from dotenv import load_dotenv
load_dotenv()

from projects import cfa_catering_message_project
from projects import cfa_cem_message_project
from projects import cfa_sales_message_project
from projects import cfa_sales_log_all_year_project
from projects import cfa_time_punch_email_project

if __name__ == '__main__':

  try: 
    if sys.argv[3] == '-h': headless = True
  except: 
    headless = False

  if sys.argv[1] == "catering-message":
    cfa_catering_message_project({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'cem-message':
    cfa_cem_message_project({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'sales-message':
    cfa_sales_message_project({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'sales-log-all-year':
    cfa_sales_log_all_year_project({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'time-punch':
    cfa_time_punch_email_project({
      'headless': headless,
      'account': sys.argv[2]
    })









