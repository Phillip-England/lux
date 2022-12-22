from datetime import date, timedelta

def get_past_date(days_in_past):
  past_date = date.today() - timedelta(days=days_in_past)
  return past_date
