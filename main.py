import os

from dotenv import load_dotenv
load_dotenv()

from destinations import cfa
from destinations import slack
from destinations import groupme
from util import failsafe

if __name__ == '__main__':

  failsafe(cfa.scripts.download_catering, options={
    'account': 'southroads',
    'dates': ['tomorrow'],
    'headless': False
  })

  failsafe(cfa.scripts.download_cems, options={
    'account': 'southroads',
    'dates': ['ytd', 'ndr', 'mtd'],
    'headless': False
  })

  catering_orders = cfa.data.get_catering(options={
    'files': ['tomorrow'],
    'account': 'southroads'
  })

  cems = cfa.data.get_cems(options={
    'files': ['ytd', 'ndr', 'mtd'],
    'account': 'southroads'
  })

  failsafe(slack.scripts.slack_message, options={
    'account': 'test',
    'message_list': cfa.messages.get_catering_list(catering_orders),
    'headless': False
  })

  failsafe(slack.scripts.slack_message, options={
    'account': 'test',
    'message_list': cfa.messages.get_cem_list(cems),
    'headless': False
  })

  failsafe(groupme.scripts.groupme_message, options={
    'account': 'test',
    'message': cfa.messages.get_catering_list(catering_orders),
    'headless': False
  })

  failsafe(groupme.scripts.groupme_message, options={
    'account': 'test',
    'message': cfa.messages.get_cem_list(cems),
    'headless': False
  })







