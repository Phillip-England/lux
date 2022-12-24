from datetime import date

def get_last_date_of_year():
  year = date.today().year
  last_date = date(year, 12, 31)
  return last_date
