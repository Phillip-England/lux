from destinations import cfa
from destinations import slack
from destinations import groupme
from util import failsafe

def cems():

  failsafe(cfa.scripts.download_cems, options={
    'account': 'southroads',
    'dates': ['ytd', 'ndr', 'mtd'],
    'headless': False
  })

  cems = cfa.data.get_cems(options={
    'files': ['ytd', 'ndr', 'mtd'],
    'account': 'southroads'
  })


  failsafe(slack.scripts.slack_message, options={
    'account': 'test',
    'message_list': cfa.messages.get_cem_list(cems),
    'headless': False
  })


  failsafe(groupme.scripts.groupme_message, options={
    'account': 'test',
    'message': cfa.messages.get_cem_list(cems),
    'headless': False
  })