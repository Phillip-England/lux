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
        'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'catering', 'tomorrow.pdf')
      }
    }
  })


  # failsafe(slack_message, options={
  #   'username': os.environ['SLACK_USERNAME'],
  #   'password': os.environ['SLACK_PASSWORD'],
  #   'account': 'test',
  #   'message': catering_message_list(catering_orders), 
  #   'channel_ids': ('C04EAJBBT4G', 'C04DZGFD9A5', 'C04EAJB016C')
  # })

  # cems = get_cems(options={
  #   'files': {
  #     'ytd': {
  #       'label': 'ytd',
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'cems', 'ytd.pdf')
  #     },
  #     'ndr': {
  #       'label': 'ndr',
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'cems', 'ndr.pdf')
  #     },
  #     'mtd': {
  #       'label': 'mtd',
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'cems', 'mtd.pdf')
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
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'cems', 'ytd.pdf')
  #     },
  #     'ndr': {
  #       'start': format_date(get_past_date(90)),
  #       'end': format_date(get_past_date(0)),
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'cems', 'ndr.pdf')
  #     },
  #     'mtd': {
  #       'start': format_date(get_first_date_of_month()),
  #       'end': format_date(get_last_date_of_month()),
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'cems', 'mtd.pdf')
  #     }
  #   }
  # })


  failsafe(groupme_message, options={
    'account': 'test',
    'message': catering_message_list(catering_orders),
    'headless': False
  })

  # failsafe(download_catering, options={
  #   'username': os.environ['SOUTHROADS_USERNAME'], 
  #   'password': os.environ['SOUTHROADS_PASSWORD'],
  #   'servicepoint_pin': os.environ['SERVICEPOINT_PIN'],
  #   'dates': {
  #     'tomorrow': {
  #       'start': format_date(get_future_date(1)),
  #       'end': format_date(get_future_date(1)),
  #       'path': os.path.join(os.getcwd(), 'downloads', 'cfa', 'southroads', 'catering', 'tomorrow.pdf')
  #     }
  #   }
  # })





