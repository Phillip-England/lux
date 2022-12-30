from scripts import cfa_download_cems_script
from scripts import slack_message_script
from scripts import groupme_message_script
from scripts import google_log_cems_script
from util import failsafe
from util import format_date
from util import get_past_date
from data import get_cems
from messages import get_cem_list

def cfa_cem_message_project(options):

  headless = options['headless']
  account = options['account']

  failsafe(cfa_download_cems_script, options={
    'account': account,
    'dates': ['ytd', 'ndr', 'mtd', 'recent'],
    'headless': headless
  })

  cems = get_cems(options={
    'files': ['ytd', 'ndr', 'mtd', 'recent'],
    'account': account
  })

  recent_cems = {
    'date': format_date(get_past_date(3)),
    'surveys': cems['recent']['surveys'],
    'osat': cems['recent']['osat'],
    'taste': cems['recent']['taste'],
    'speed': cems['recent']['speed'],
    'ace': cems['recent']['ace'],
    'clean': cems['recent']['clean'],
    'accuracy': cems['recent']['accuracy'],
  }

  if account != 'test':
    failsafe(google_log_cems_script, options={
      'data': recent_cems,
      'headless': headless
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