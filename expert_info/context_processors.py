import datetime

def general_info(request):
    today = datetime.datetime.now()

    day = today.day
    month = today.month
    year = today.year

    hour = today.hour
    minutes = today.minute

    return dict(day=day,month=month,year=year,hour=hour,minutes=minutes)
