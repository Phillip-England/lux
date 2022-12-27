import datetime

def get_days_from_first_of_year():
  today = datetime.datetime.now()
  current_year = today.year
  first_of_year = datetime.datetime(current_year, 1, 1)
  return (today - first_of_year).days
