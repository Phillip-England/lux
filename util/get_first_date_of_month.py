from datetime import date

def get_first_date_of_month():
  year = date.today().year
  month = date.today().month
  first_date = date(year, month, 1)
  return first_date