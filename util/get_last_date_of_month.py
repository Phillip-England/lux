from datetime import date, timedelta

def get_last_date_of_month():
  year = date.today().year
  month = date.today().month
  if month == 12:
    next_month_first_date = date(year+1, 1, 1)
    last_date = next_month_first_date - timedelta(days=1)
  else:
    next_month_first_date = date(year, month+1, 1)
    last_date = next_month_first_date - timedelta(days=1)
  return last_date

