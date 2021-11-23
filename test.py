from croniter import croniter
from datetime import datetime


str_time_now=datetime.now()

iter=croniter("00 08 * * *",str_time_now)

print(iter.get_next(datetime))