import datetime

x = datetime.datetime.now()

y=str(x.strftime("%H:%M:%S"))
fmt = "%H:%M:%S"
time1 = datetime.datetime.strptime(y,fmt)

print(time1)