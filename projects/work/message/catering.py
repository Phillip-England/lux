import os

from destinations import cfa
from destinations import groupme
from destinations import slack
from util import failsafe

def catering(options):

  headless = options['headless']
  account = options['account']

  download_paths = failsafe(cfa.scripts.download_catering, options={
    'account': account,
    'dates': ['tomorrow'],
    'headless': headless
  })
  
  if len(download_paths) != 0:

    catering_orders = cfa.data.get_catering(options={
      'files': ['tomorrow'],
      'account': account
    })

    failsafe(slack.scripts.slack_message, options={
      'account': account,
      'message_list': cfa.messages.get_catering_list(catering_orders),
      'headless': headless
    })

    failsafe(groupme.scripts.groupme_message, options={
      'account': account,
      'message': cfa.messages.get_catering_list(catering_orders),
      'headless': headless
    })




