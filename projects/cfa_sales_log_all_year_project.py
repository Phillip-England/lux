import os

from util import failsafe
from util import get_days_from_first_of_year
from util import format_date
from util import get_past_date
from scripts import cfa_download_sales_script
from scripts import google_log_sales_script
from data import extract_daypart_activity

def cfa_sales_log_all_year_project(options):
  
  headless = options['headless']
  account = options['account']
  daypart_activity_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'daypart_activity.pdf')

  days_from_first_of_year = get_days_from_first_of_year()

  while days_from_first_of_year != 0:
    
    is_downloaded = failsafe(cfa_download_sales_script, options={
      'account': account,
      'start_date': format_date(get_past_date(days_from_first_of_year)),
      'end_date': format_date(get_past_date(days_from_first_of_year)),
      'download_path': daypart_activity_path,
      'headless': headless 
    })

    days_from_first_of_year -= 1

    if is_downloaded:

      sales_data = extract_daypart_activity(daypart_activity_path)

      failsafe(google_log_sales_script, options={
        'data': sales_data,
        'headless': headless,
        'account': account
      })

       


