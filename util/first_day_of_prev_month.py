import datetime

def first_day_of_prev_month() -> datetime.date:
    today = datetime.date.today()
    if today.month == 1:
        return datetime.date(today.year - 1, 12, 1)
    else:
        return datetime.date(today.year, today.month - 1, 1)
