import os

from util import failsafe
from util import get_past_date
from util import format_date
from scripts import cfa_download_sales_script
from scripts import slack_message_script
from scripts import groupme_message_script
from scripts import google_log_sales_script
from data import extract_daypart_activity
from messages import get_sales_list

def cfa_sales_message_project(options):

  headless = options['headless']
  account = options['account']
  daypart_activity_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'daypart_activity.pdf')


  is_downloaded = failsafe(cfa_download_sales_script, options={
    'account': account,
    'start_date': format_date(get_past_date(1)),
    'end_date': format_date(get_past_date(1)),
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

    sales_message = get_sales_list(daypart_activity_data)

    # failsafe(slack_message_script, options={
    #   'account': account,
    #   'message_list': sales_message,
    #   'headless': headless
    # })

    failsafe(groupme_message_script, options={
      'account': account,
      'message': sales_message,
      'headless': headless
    })


