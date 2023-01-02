import datetime

def get_current_month():
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Get the month as an integer (1-12)
    month = now.month
    
    # Define a list of month names
    month_names = ["January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    
    # Return the month name
    return month_names[month-1]
