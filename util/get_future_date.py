import datetime

def get_future_date(days_in_future):
    current_date = datetime.datetime.now()
    delta = datetime.timedelta(days=days_in_future)
    future_date = current_date + delta
    return future_date.date()
