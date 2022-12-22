import os

from dotenv import load_dotenv
load_dotenv()

from lux.failsafe import failsafe

from scripts.cfa.download_cems import download_cems
from scripts.groupme.groupme_message import groupme_message
from scripts.cfa.download_catering import download_catering
from scripts.slack.slack_message import slack_message

from data.get_cems import get_cems
from data.get_catering import get_catering

from message.catering_message_list import catering_message_list
from message.cem_message_list import cem_message_list

from date.format_date import format_date
from date.get_first_date_of_month import get_first_date_of_month
from date.get_last_date_of_month import get_last_date_of_month
from date.get_first_date_of_year import get_first_date_of_year
from date.get_last_date_of_year import get_last_date_of_year
from date.get_past_date import get_past_date
from date.get_future_date import get_future_date

if __name__ == '__main__':


  catering_orders = get_catering(options={
    'files': {
      'tomorrow': {
        'label': 'tomorrow',
        'path': './downloads/cfa/southroads/catering/tomorrow.pdf'
      }
    }
  })

  failsafe(slack_message, options={
    'username': os.environ['SLACK_USERNAME'],
    'password': os.environ['SLACK_PASSWORD'],
    'workspace_url': 'https://testing-hkz9125.slack.com'
  })

  # cems = get_cems(options={
  #   'files': {
  #     'ytd': {
  #       'label': 'ytd',
  #       'path': './downloads/cfa/southroads/cems/ytd.pdf'
  #     },
  #     'ndr': {
  #       'label': 'ndr',
  #       'path': './downloads/cfa/southroads/cems/ndr.pdf'
  #     },
  #     'mtd': {
  #       'label': 'mtd',
  #       'path': './downloads/cfa/southroads/cems/mtd.pdf'
  #     }
  #   }
  # })


  # failsafe(download_cems, options={
  #   'username': os.environ['SOUTHROADS_USERNAME'], 
  #   'password': os.environ['SOUTHROADS_PASSWORD'],
  #   'dates': {
  #     'ytd': {
  #       'start': format_date(get_first_date_of_year()),
  #       'end': format_date(get_last_date_of_year()),
  #       'path': f'./downloads/cfa/southroads/cems/ytd.pdf',
  #     },
  #     'ndr': {
  #       'start': format_date(get_past_date(90)),
  #       'end': format_date(get_past_date(0)),
  #       'path': f'./downloads/cfa/southroads/cems/ndr.pdf'
  #     },
  #     'mtd': {
  #       'start': format_date(get_first_date_of_month()),
  #       'end': format_date(get_last_date_of_month()),
  #       'path': f'./downloads/cfa/southroads/cems/mtd.pdf'
  #     }
  #   }
  # })


  # failsafe(groupme_message, options={
  #   'username': os.environ['GROUPME_TESTING_USERNAME'], 
  #   'password': os.environ['GROUPME_TESTING_PASSWORD'], 
  #   'chat_label': 'Chat testing',
  #   'message': catering_message_list(catering_orders)
  # })

  # failsafe(download_catering, options={
  #   'username': os.environ['SOUTHROADS_USERNAME'], 
  #   'password': os.environ['SOUTHROADS_PASSWORD'],
  #   'servicepoint_pin': os.environ['SERVICEPOINT_PIN'],
  #   'dates': {
  #     'tomorrow': {
  #       'start': format_date(get_future_date(1)),
  #       'end': format_date(get_future_date(1)),
  #       'path': './downloads/cfa/southroads/catering/tomorrow.pdf'
  #     }
  #   }
  # })





