from datetime import date

def get_date_object(date_str):
    slashes_found = 0
    month = ''
    day = ''
    year = ''
    for character in date_str:
        if character == '/':
            slashes_found += 1
        else:
            if slashes_found == 0:
                month += character
            if slashes_found == 1:
                day += character
            if slashes_found == 2:
                year += character
    return date(int(year), int(month), int(day))