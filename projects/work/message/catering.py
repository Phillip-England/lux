import os

from destinations import cfa
from destinations import groupme
from destinations import slack
from util import failsafe

def catering():

  download_paths = failsafe(cfa.scripts.download_catering, options={
    'account': 'southroads',
    'dates': ['tomorrow'],
    'headless': True
  })


  for path in download_paths:
    if os.path.exists(path):
      pass
    else:
      download_paths.remove(path)
  
  print(download_paths)

  # try:

  #   catering_orders = cfa.data.get_catering(options={
  #     'files': ['tomorrow'],
  #     'account': 'southroads'
  #   })

  #   failsafe(slack.scripts.slack_message, options={
  #     'account': 'test',
  #     'message_list': cfa.messages.get_catering_list(catering_orders),
  #     'headless': False
  #   })

  #   failsafe(groupme.scripts.groupme_message, options={
  #     'account': 'test',
  #     'message': cfa.messages.get_catering_list(catering_orders),
  #     'headless': False
  #   })

  # except:

  #   print("No catering for tomorrow")



