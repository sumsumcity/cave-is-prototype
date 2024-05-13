import datetime

def now():
    result = datetime.datetime.now(datetime.timezone.utc)
    return result