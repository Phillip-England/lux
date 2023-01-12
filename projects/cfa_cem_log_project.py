import os

from scripts import cfa_download_cems_script
from scripts import google_log_cems_script

from data import extract_cem_units
from data import extract_cem_time_of_day
from data import extract_cem_type_of_visit
from data import format_cems_for_logging

from util import failsafe
from util import get_date_object
from util import get_day_of_week

def cfa_cem_log_project(options):

  account = options['account']
  headless = options['headless']
  date = options['date']

  # recent cem paths
  custom_units_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'custom_units.html')
  custom_time_of_day_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'custom_time_of_day.html')
  custom_type_of_visit_cem_path = os.path.join(os.environ["PROJECT_PATH"], 'downloads', 'cfa', f'{account}', 'cems', 'custom_type_of_visit.html')

  file_paths = {
    'custom_units_cem_path': custom_units_cem_path,
    'custom_time_of_day_cem_path': custom_time_of_day_cem_path,
    'custom_type_of_visit_cem_path': custom_type_of_visit_cem_path,
  }

  failsafe(cfa_download_cems_script, options={
    'account': account,
    'headless': headless,
    'file_paths': file_paths,
    'date': date
  })

  custom_units = extract_cem_units(custom_units_cem_path)
  custom_time_of_day = extract_cem_time_of_day(custom_time_of_day_cem_path)
  custom_type_of_visit = extract_cem_type_of_visit(custom_type_of_visit_cem_path)

  cems_for_logging = format_cems_for_logging(custom_units, custom_time_of_day, custom_type_of_visit)


  failsafe(google_log_cems_script, options={
    'data': cems_for_logging,
    'headless': headless,
    'account': account
  })



