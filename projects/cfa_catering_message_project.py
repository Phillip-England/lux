import os

from util import failsafe
from scripts import cfa_download_catering_script
from scripts import slack_message_script
from scripts import groupme_message_script
from data import get_catering
from messages import get_catering_list

def cfa_catering_message_project(options):

  headless = options['headless']
  account = options['account']

  download_paths = failsafe(cfa_download_catering_script, options={
    'account': account,
    'dates': ['tomorrow'],
    'headless': headless
  })
  
  if len(download_paths) != 0:

    catering_orders = get_catering(options={
      'files': ['tomorrow'],
      'account': account
    })

    failsafe(slack_message_script, options={
      'account': account,
      'message_list': get_catering_list(catering_orders),
      'headless': headless
    })

    failsafe(groupme_message_script, options={
      'account': account,
      'message': get_catering_list(catering_orders),
      'headless': headless
    })




