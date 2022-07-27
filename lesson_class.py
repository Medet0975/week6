class ItSchool:
    bootcamp = 15000
    time = "8:30"

kunduz = ItSchool()
yasir = ItSchool()
timur = ItSchool()

kunduz.free = True
print(kunduz.__dict__)


# print(ItSchool.__dict__)
# yasir.bootcamp = 15000
# yasir.free = True
# print(yasir.__dict__)
# print()
# print(timur.__dict__)


# class CarCarolla:
#     wheels = 4
#     volume = 1.8
#     engine = "v6"
#     kuzov = "sedan"
#
#     def __init__(self, bumper, color, otdelka):
#         self.bumper = bumper
#         self.color = color
#         self.otdelka = otdelka
#
#     def get_info(self):
#         print(f" {self.bumper} , цвет машины: {self.color} , отделка машины: {self.otdelka} ")
#
#     def change_otdelka(self, new_otdelka):
#         self.otdelka = new_otdelka
#
#     def get_hello(self):
#         print("Hello world")
#
#
# mirlan = CarCarolla("m obves", "white", "alkantaro")
# # andrey = CarCarolla("v obves", "dark blue", "krokodile")
#
#
# mirlan.get_info()
# mirlan.change_otdelka("alpaka")
# mirlan.get_info()
#
# mirlan.get_hello()
# andrey.get_info()

# print(mirlan.__dict__)
# print(andrey.__dict__)

# print(mirlan.bumper)
# print(mirlan.color)
# print(mirlan.otdelka)
# print(mirlan.engine)


# lessons_timur = {
#     "peremennye": 100,
#     "loop": 87,
#     "func": 58,
# }
#
# lessons_nasyikat = {
#     "peremennye": 100,
#     "loop": 90,
#     "func": 79,
# }
#
# lessons_aliya = {
#     "peremennye": 100,
#     "loop": 90,
#     "func": 79,
# }
#
# class Student:
#     group = "python_bootcamp_8_30"
#     def __init__(self, full_name, age, phone_number, lesson):
#         self.full_name = full_name
#         self.age = age
#         self.phone_number = phone_number
#         self.lesson =lesson
#         self.avg =0
#
#     def get_info(self):
#         print(f" Группа: Python 8:30 Зовут {self.full_name} возраст: {self.age} "
#               f"номер телефона: {self.phone_number} средний балл: {self.avg}")
#
#     def set_avg(self):
#         result = sum(self.lesson.values()) / len(self.lesson)
#         self.avg = round(result)
#
#     def set_avg_2(self):
#         sum = 0
#         for i in self.lesson.values():
#         #     sum += i
#         # self.avg = round(sum / len(self.lesson))
#         # print(sum)
#             sum = sum + i
#         result = sum / len(self.lesson)
#         self.avg = result






# timur = Student("Насирдинов Тимур", 18, "996555443322", lessons_timur)
# nasyikat = Student("Арзыбаева Насыйкат", 38, "996555888888", lessons_nasyikat)
# aliya = Student("Нарынбекова Алия", 21, "996555555555", lessons_aliya)
# timur.get_info()
# timur.set_avg_2()
# timur.get_info()