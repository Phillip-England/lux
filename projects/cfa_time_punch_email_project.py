from util import failsafe
from scripts import cfa_download_time_punch_script

def cfa_time_punch_email_project(options):

  headless = options['headless']
  account = options['account']

  failsafe(cfa_download_time_punch_script, options={
    'headless': headless,
    'account': account
  })

