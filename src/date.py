from datetime import datetime, timedelta

def areSameDatetime(datetime1: datetime, datetime2: datetime):
    return datetime1 == datetime2

def areSameDate(datetime1: datetime, datetime2: datetime):
    difference = datetime1.date() - datetime2.date()
    return difference == timedelta(days=0)

def areSameTime(datetime1: datetime, datetime2: datetime):
    return datetime1.time() == datetime2.time()

def newDatetime(year, month, day, hour, min):
    newDate = datetime(year= year, month= month, day= day, hour= hour, minute= min)
    return removeSecondsAndMicroseconds(newDate)

def datetimeFromTimestamp(timestamp: int):
    auxDtme = datetime.fromtimestamp(timestamp)
    return removeSecondsAndMicroseconds(auxDtme)

def now():
    now = datetime.now()
    return removeSecondsAndMicroseconds(now)

def today():
    today = datetime.now().replace(hour=0, minute=0)
    return removeSecondsAndMicroseconds(today)

def removeSecondsAndMicroseconds(aux: datetime):
    return aux.replace(second=0, microsecond=0)
