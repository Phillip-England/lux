from datetime import date

def get_first_date_of_year():
  year = date.today().year
  first_date = date(year, 1, 1)
  return first_date
