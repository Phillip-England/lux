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

  failsafe(download_catering, options={
    'account': 'southroads',
    'dates': ['tomorrow'],
    'headless': False
  })

  failsafe(download_cems, options={
    'account': 'southroads',
    'dates': ['ytd', 'ndr', 'mtd'],
    'headless': False
  })

  catering_orders = get_catering(options={
    'files': ['tomorrow'],
    'account': 'southroads'
  })

  cems = get_cems(options={
    'files': ['ytd', 'ndr', 'mtd'],
    'account': 'southroads'
  })

  failsafe(slack_message, options={
    'account': 'test',
    'message_list': catering_message_list(catering_orders),
    'headless': False
  })

  failsafe(slack_message, options={
    'account': 'test',
    'message_list': cem_message_list(cems),
    'headless': False
  })

  failsafe(groupme_message, options={
    'account': 'test',
    'message': catering_message_list(catering_orders),
    'headless': False
  })

  failsafe(groupme_message, options={
    'account': 'test',
    'message': cem_message_list(cems),
    'headless': False
  })







