import os

from scripts import cfa_download_cems_script
from scripts import google_log_cems_script
# from data import extract_cem_scores
from util import failsafe
from util import pdf_to_text
from util import get_date_object
from util import get_day_of_week
from util import format_date
from util import get_past_date

def cfa_cem_log_project(options):
  account = options['account']
  headless = options['headless']
  date = options['date']
  custom_cem_download_path = os.path.join(os.environ['PROJECT_PATH'], 'downloads', 'cfa', f'{account}', 'cems', 'custom.pdf')

  failsafe(cfa_download_cems_script, options={
    'account': account,
    'dates': {
      'custom': {
        'path': custom_cem_download_path,
        'start_date': date,
        'end_date': date
      }
    },
    'headless': headless
  })

  cems = {
    # 'custom': extract_cem_scores(pdf_to_text(custom_cem_download_path)),
  }

  date_object = get_date_object(date)
  day_of_week = get_day_of_week(date_object)

  custom_cems = {
    'date': date,
    'day_of_week': day_of_week,
    'surveys': cems['custom']['surveys'],
    'osat': cems['custom']['osat'],
    'taste': cems['custom']['taste'],
    'speed': cems['custom']['speed'],
    'ace': cems['custom']['ace'],
    'clean': cems['custom']['clean'],
    'accuracy': cems['custom']['accuracy'],
  }

  failsafe(google_log_cems_script, options={
    'data': custom_cems,
    'headless': headless,
    'account': account
  })



