import datetime

a = datetime.datetime.now()
b = a-datetime.timedelta(1)
print((a-b).days*3600*24,"seconds difference") # note: 1 day = 24 hours, 1 hour = 60 minutes = 3600 seconds