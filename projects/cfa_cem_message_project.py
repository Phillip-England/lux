import os

from scripts import cfa_download_cems_script
from scripts import slack_message_script
from scripts import groupme_message_script
from scripts import google_log_cems_script
from scripts import signpresenter_post_cem_scorecard_script

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

from data import generate_cem_scorecard
from data import extract_cem_units
from data import extract_cem_time_of_day
from data import extract_cem_type_of_visit
from data import format_cems_for_logging
from data import format_cems_for_messaging

from messages import get_cem_list

def cfa_cem_message_project(options):

  headless = options['headless']
  account = options['account']

  # recent cem paths
  recent_units_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'recent_units.html')
  recent_time_of_day_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'recent_time_of_day.html')
  recent_type_of_visit_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'recent_type_of_visit.html')

  # mtd cem paths
  mtd_units_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'mtd_units.html')

  # pm cem paths
  pm_units_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'pm_units.html')

  # ndr cem paths  
  ndr_units_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'ndr_units.html')

  # ytd cem paths  
  ytd_units_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'ytd_units.html')

  file_paths = {
    'recent_units_cem_path': recent_units_cem_path,
    'recent_time_of_day_cem_path': recent_time_of_day_cem_path,
    'recent_type_of_visit_cem_path': recent_type_of_visit_cem_path,
    'mtd_units_cem_path': mtd_units_cem_path,
    'pm_units_cem_path': pm_units_cem_path,
    'ndr_units_cem_path': ndr_units_cem_path,
    'ytd_units_cem_path': ytd_units_cem_path
  }

  # failsafe(cfa_download_cems_script, options={
  #   'account': account,
  #   'headless': headless,
  #   'file_paths': file_paths
  # })

  recent_units = extract_cem_units(recent_units_cem_path)
  recent_time_of_day = extract_cem_time_of_day(recent_time_of_day_cem_path)
  recent_type_of_visit = extract_cem_type_of_visit(recent_type_of_visit_cem_path)
  mtd_units = extract_cem_units(mtd_units_cem_path)
  pm_units = extract_cem_units(pm_units_cem_path)
  ndr_units = extract_cem_units(ndr_units_cem_path)
  ytd_units = extract_cem_units(ytd_units_cem_path)

  # generate_cem_scorecard({
  #   'account': account,
  #   'mtd_cems': mtd_units,
  # })

  # failsafe(signpresenter_post_cem_scorecard_script, options={
  #   'account': account,
  #   'headless': headless
  # })


  # cems_for_logging = format_cems_for_logging(recent_units, recent_time_of_day, recent_type_of_visit)


  # failsafe(google_log_cems_script, options={
  #   'data': cems_for_logging,
  #   'headless': headless,
  #   'account': account
  # })

  # failsafe(slack_message_script, options={
  #   'account': account,
  #   'message_list': get_cem_list(cems),
  #   'headless': headless
  # })

  cems_for_messaging = format_cems_for_messaging(mtd_units, ndr_units, ytd_units)
  cem_message = get_cem_list(cems_for_messaging)


  failsafe(groupme_message_script, options={
    'account': account,
    'message': cem_message,
    'headless': headless
  })

  