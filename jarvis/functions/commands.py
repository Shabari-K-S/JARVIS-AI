import calendar
from datetime import datetime


# Here the start of calendar and time functions

def get_day_of_week():
    day = datetime.now().weekday()
    return calendar.day_name[day]

def get_date():
    return datetime.now().strftime("%B %d, %Y")

def get_time():
    return datetime.now().strftime("%I:%M %p")

def get_month():
    return datetime.now().strftime("%B")

def get_year():
    return datetime.now().strftime("%Y")

def check_calender_cmd(command):
    if "day of the week" in command.lower():
        day = get_day_of_week()
        print(day)
        return True, day
    elif "what date" in command.lower() or "current date" in command.lower() or "what is the date" in command.lower():
        date = get_date()
        print(date)
        return True, date
    elif "what time" in command.lower() or "current time" in command.lower() or "what is the time" in command.lower():
        time = get_time()
        print(time)
        return True, time
    elif "what month" in command.lower() or "current month" in command.lower() or "what is the month" in command.lower():
        month = get_month()
        print(month)
        return True, month
    elif "what year" in command.lower() or "current year" in command.lower() or "what is the year" in command.lower():
        year = get_year()
        print(year)
        return True, year
    else:
        return False, ""
    
# Here the end of calendar and time functions
