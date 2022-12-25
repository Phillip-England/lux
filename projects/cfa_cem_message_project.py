from scripts import cfa_download_cems_script
from scripts import slack_message_script
from scripts import groupme_message_script
from util import failsafe
from data import get_cems
from messages import get_cem_list

def cfa_cem_message_project(options):

  headless = options['headless']
  account = options['account']

  failsafe(cfa_download_cems_script, options={
    'account': account,
    'dates': ['ytd', 'ndr', 'mtd'],
    'headless': headless
  })

  cems = get_cems(options={
    'files': ['ytd', 'ndr', 'mtd'],
    'account': account
  })

  failsafe(slack_message_script, options={
    'account': account,
    'message_list': get_cem_list(cems),
    'headless': headless
  })


  failsafe(groupme_message_script, options={
    'account': account,
    'message': get_cem_list(cems),
    'headless': headless
  })