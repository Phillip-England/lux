import os

from data import extract_time_punch
from util import failsafe
from util import pdf_to_text
from util import email_sender
from scripts import cfa_download_time_punch_script
from scripts import cfa_download_employee_bio_script

def cfa_time_punch_email_project(options):

  headless = options['headless']
  account = options['account']

  if account == 'test':
    send_to = os.environ['PERSONAL_EMAIL']

  if account == 'southroads':
    send_to = os.environ['SOUTHROADS_EMAIL']

  # download_path = failsafe(cfa_download_time_punch_script, options={
  #   'headless': headless,
  #   'account': account
  # })

  # employee_names = failsafe(cfa_download_employee_bio_script, options={
  #   'headless': headless,
  #   'account': account
  # })

  download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'time-punch', 'punch.pdf')

  time_punch_message = extract_time_punch(pdf_to_text(download_path))

  print(time_punch_message)

  email_sender({
    'email': os.environ['AUTOMATION_EMAIL'],
    'password': os.environ['AUTOMATION_EMAIL_PASSWORD'],
    'send_to': send_to,
    'subject': 'Time Punch Report Automation',
    'message': time_punch_message
  })
