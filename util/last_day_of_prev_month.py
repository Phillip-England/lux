import datetime

def last_day_of_prev_month() -> datetime.date:
    today = datetime.date.today()
    first_day_of_current_month = datetime.date(today.year, today.month, 1)
    last_day_of_prev_month = first_day_of_current_month - datetime.timedelta(days=1)
    return last_day_of_prev_month
