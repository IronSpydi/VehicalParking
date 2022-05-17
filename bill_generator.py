from datetime import datetime
import time

x = datetime.now()
print(x)
time.sleep(30)
y = datetime.now()
print(y)
z = y - x
print(z.seconds)