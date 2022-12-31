import os

from util import failsafe
from scripts import cfa_download_sales_script
from scripts import google_log_sales_script
from data import extract_daypart_activity


def cfa_sales_log_project(options):

  headless = options['headless']
  account = options['account']
  date = options['date']
  daypart_activity_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'daypart_activity.pdf')

  is_downloaded = failsafe(cfa_download_sales_script, options={
    'account': account,
    'start_date': date,
    'end_date': date,
    'download_path': daypart_activity_path,
    'headless': headless
  })


  if is_downloaded:

    daypart_activity_data = extract_daypart_activity(daypart_activity_path)

    failsafe(google_log_sales_script, options={
      'data': daypart_activity_data,
      'headless': headless,
      'account': account
    })