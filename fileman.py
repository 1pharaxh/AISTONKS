import os
from datetime import datetime, timedelta
from threading import Timer
def filemgmt():
    for filename in os.listdir("static/images"):
        if filename.endswith(".jpg"):
            os.remove(os.path.join("static/images", filename))
    for filename in os.listdir():
        if filename.endswith(".csv"):
            os.remove(filename)
    for filename in os.listdir():
        if filename.endswith(".pickle"):
            os.remove(filename)

def cleanup(func):
    currnday=datetime.today()
    dateLog = currnday.replace(day=currnday.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(days=1)
    delta_t=dateLog-currnday

    secs=delta_t.total_seconds()

    t = Timer(secs, func)
    t.start()