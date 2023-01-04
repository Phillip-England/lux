import os

from scripts import cfa_download_cems_script
from scripts import slack_message_script
from scripts import groupme_message_script
from scripts import google_log_cems_script
from scripts import signpresenter_post_cem_scorecard_script
from data import generate_cem_scorecard
from util import failsafe
from util import format_date
from util import get_past_date
from util import pdf_to_text
from util import get_date_object
from util import get_day_of_week
from util import get_first_date_of_year
from util import get_last_date_of_year
from util import get_first_date_of_month
from util import get_last_date_of_month
from util import last_day_of_prev_month
from util import first_day_of_prev_month
from data import extract_cem_scores
from messages import get_cem_list

def cfa_cem_message_project(options):

  headless = options['headless']
  account = options['account']

  ytd_cem_download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'ytd.pdf')
  ndr_cem_download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'ndr.pdf')
  mtd_cem_download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'mtd.pdf')
  recent_cem_download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'recent.pdf')
  pm_cem_download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'pm.pdf')
  day_of_week = format_date(get_day_of_week(3))
  recent_date = format_date(get_past_date(3))

  failsafe(cfa_download_cems_script, options={
    'account': account,
    'headless': headless,
    'dates': {
      'ytd': {
        'path': ytd_cem_download_path,
        'start_date': format_date(get_first_date_of_year()),
        'end_date': format_date(get_last_date_of_year())
      },
      'mtd': {
        'path': mtd_cem_download_path,
        'start_date': format_date(get_first_date_of_month()),
        'end_date': format_date(get_last_date_of_month())
      },
      'ndr': {
        'path': ndr_cem_download_path,
        'start_date': format_date(get_past_date(90)),
        'end_date': format_date(get_past_date(0))
      },
      'recent': {
        'path': recent_cem_download_path,
        'start_date': recent_date,
        'end_date': recent_date
      },
      'pm': {
        'path': pm_cem_download_path,
        'start_date': format_date(first_day_of_prev_month()),
        'end_date': format_date(last_day_of_prev_month())
      }
    },
  })

  cems = {
    'ytd': extract_cem_scores(pdf_to_text(ytd_cem_download_path)),
    'ndr': extract_cem_scores(pdf_to_text(ndr_cem_download_path)),
    'mtd': extract_cem_scores(pdf_to_text(mtd_cem_download_path)),
    'recent': extract_cem_scores(pdf_to_text(recent_cem_download_path)),
    'pm': extract_cem_scores(pdf_to_text(pm_cem_download_path)),
  }

  generate_cem_scorecard({
    'account': account,
    'mtd_cems': cems['mtd'],
  })

  failsafe(signpresenter_post_cem_scorecard_script, options={
    'account': account,
    'headless': headless
  })

  recent_cems = {
    'date': recent_date,
    'day_of_week': day_of_week,
    'surveys': cems['recent']['surveys'],
    'osat': cems['recent']['osat'],
    'taste': cems['recent']['taste'],
    'speed': cems['recent']['speed'],
    'ace': cems['recent']['ace'],
    'clean': cems['recent']['clean'],
    'accuracy': cems['recent']['accuracy'],
  }

  failsafe(google_log_cems_script, options={
    'data': recent_cems,
    'headless': headless,
    'account': account
  })

  # failsafe(slack_message_script, options={
  #   'account': account,
  #   'message_list': get_cem_list(cems),
  #   'headless': headless
  # })

  failsafe(groupme_message_script, options={
    'account': account,
    'message': get_cem_list(cems),
    'headless': headless
  })

  