# datetime

import datetime
from datetime import timedelta


now = datetime.datetime.now()
date_2 = datetime.date(2022, 5, 25)
print(type(date_2))
# new_time = now.date() - now.time()
# new_time = now.date() - date_2
# print(now)
# print(now.date())
# print(now.time())
#
# print(new_time)

time_2 = datetime.time(13, 30)
print(time_2)
# new_time = time_2 - now.time()
# print(new_time)

all_data= datetime.datetime.combine(date_2, time_2)
print(now.strftime('%a'))
print(all_data.strftime('%A'))
print(all_data.strftime('%a'))


days = 30
now = datetime.datetime.now()
end_date = now.date() + timedelta(days)
print(end_date)



