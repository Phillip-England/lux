import os


from util import failsafe
from util import get_past_date
from util import format_date
from util import pdf_to_text
from scripts import cfa_download_sales_script
from scripts import slack_message_script
from scripts import groupme_message_script
from scripts import google_sales_form_script
from data import extract_sales
from messages import get_sales_list

def cfa_sales_message_project(options):

  headless = options['headless']
  account = options['account']
  download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'sales', 'test.pdf')

  # is_downloaded = failsafe(cfa_download_sales_script, options={
  #   'account': account,
  #   'start_date': format_date(get_past_date(5)),
  #   'end_date': format_date(get_past_date(5)),
  #   'download_path': download_path,
  #   'headless': headless
  # })

  is_downloaded = True

  if is_downloaded:

    sales_data = extract_sales(download_path)

    

    # failsafe(google_sales_form_script, options={
    #   'data': sales_data,
    #   'headless': headless
    # })

    # sales_message = get_sales_list(sales_data)

    # failsafe(slack_message_script, options={
    #   'account': account,
    #   'message_list': sales_message,
    #   'headless': headless
    # })


    # failsafe(groupme_message_script, options={
    #   'account': account,
    #   'message': sales_message,
    #   'headless': headless
    # })


