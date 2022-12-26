from util import failsafe
from scripts import cfa_download_sales_script
from scripts import slack_message_script
from scripts import groupme_message_script
from data import get_sales
from messages import get_sales_list

def cfa_sales_message_project(options):

  headless = options['headless']
  account = options['account']

  download_paths = failsafe(cfa_download_sales_script, options={
    'account': account,
    'dates': ['yesterday'],
    'headless': headless
  })

  if len(download_paths) != 0:

    sales_data = get_sales(options={
      'files': ['yesterday'],
      'account': account
    })

    sales_message = get_sales_list(sales_data)

    failsafe(slack_message_script, options={
      'account': account,
      'message_list': sales_message,
      'headless': headless
    })


    failsafe(groupme_message_script, options={
      'account': account,
      'message': sales_message,
      'headless': headless
    })

