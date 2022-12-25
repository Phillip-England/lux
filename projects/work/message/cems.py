from destinations import cfa
from destinations import slack
from destinations import groupme
from util import failsafe

def cems(options):

  headless = options['headless']
  account = options['account']

  failsafe(cfa.scripts.download_cems, options={
    'account': account,
    'dates': ['ytd', 'ndr', 'mtd'],
    'headless': headless
  })

  cems = cfa.data.get_cems(options={
    'files': ['ytd', 'ndr', 'mtd'],
    'account': account
  })

  failsafe(slack.scripts.slack_message, options={
    'account': account,
    'message_list': cfa.messages.get_cem_list(cems),
    'headless': headless
  })


  failsafe(groupme.scripts.groupme_message, options={
    'account': account,
    'message': cfa.messages.get_cem_list(cems),
    'headless': headless
  })