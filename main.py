import os
import sys

from dotenv import load_dotenv
load_dotenv()

from projects import cfa_catering_message_project
from projects import cfa_cem_message_project
from projects import cfa_sales_message_project
from projects import cfa_sales_log_all_year_project
from projects import cfa_time_punch_email_project
from projects import cfa_sales_log_project
from projects import cfa_cem_log_project
from projects import cfa_scorecard_project

if __name__ == '__main__':

  if '-h' in sys.argv: headless = True
  else: headless = False

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

  if sys.argv[1] == 'cem-log':
    cfa_cem_log_project({
      'headless': headless,
      'account': sys.argv[2],
      'date': sys.argv[3]
    })

  if sys.argv[1] == 'sales-message':
    cfa_sales_message_project({
      'headless': headless,
      'account': sys.argv[2]
    })

  if sys.argv[1] == 'sales-log':
    cfa_sales_log_project({
      'headless': headless,
      'account': sys.argv[2],
      'date': sys.argv[3]
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

  if sys.argv[1] == 'scorecard':
    cfa_scorecard_project({
      'headless': headless,
      'account': sys.argv[2]
    })
  









