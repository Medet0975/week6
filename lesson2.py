import datetime
from datetime import timedelta

# def get.time(days):

date = datetime.date(2022, 6, 22)
# days = 30
# date_2 = date +timedelta(days)
# print(f'{date_2}")
# print(f'{date_2}, "Конец 1 этапа"')
# elif days == 60:


# def devide_time(date):
#     stage1 = date + timedelta(30)
#     stage2 = stage1 + timedelta(20)
#     stage3 = stage2 + timedelta(50)
#     print((f"{stage1} Конец первого этапа"))
#     print((f"{stage1} Конец второго этапа"))
#     print((f"{stage1} Защита!"))
#     return stage1, stage2, stage3
#
# a = devide_time(date)
# print(a)


# lists = ["ps4", "data", "ll", "warkraft"]
#
# def devide_time(renting, product_item):
#     now = datetime.datetime.now()
#     item_time = now + timedelta(renting)
#
#     print(f"{product_item}  должны возвратить {item_time}")
#     return {
#         f"{product_item}": item_time
#     }
#
# a = devide_time((2, lists[0]))
dt_string = "12/11/2018 09:15:32"
print(datetime.datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S"))

now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(datetime.datetime.timestamp(now))


day_3 = datetime.date(1975, 10, 9)
print(datetime.datetime.timestamp(date_3)

# timestamp = 1
# dt_object = datetime.datetime.fromtimestamp(timestamp)
# print(dt_object)