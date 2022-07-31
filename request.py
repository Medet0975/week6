import requests
#
# res = requests.get('https://24.kg')
#
# if res:
#     print('Response OK')
# else:
#     print('Response Failed')
#
# # print(res.status_code)
# # print(res.headers)
# print(res.text)
# url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
# API_KEY = 'your yandex api key'
# res = requests.get(url)
# params = dict(key=API_KEY, text='Hello', lang='en-es')
# res = requests.get(url, params=params)
# print(res.status_code)
# print(res)
# print(res.text)
# print(res.headers)
# json = res.json()
# print(json)

#
# def test ():
#     print('______________________')
# test()


class Product:
    __name = None
    __price = None
    __weight = None

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight


class Buy(Product):
    def __init__(self):
        self.__kol = None
        # self.__total_price = None
        # self.__total_weight = None

    def set_total_price(self):
        self.total_price = self.kol * self.get_price()
        return self.total_price

    def set_kol(self, kol):
        self.kol = kol
        return self.kol

    def set_total_weight(self):
        # self.total_weight = self.kol * self.get_weight()
        self.total_weight = self.kol
        return self.total_weight

class Check(Buy):

    def get_info(self):
        print(f"name: {self.get_name()}, "
              f"kol: {self.kol}, "
              f"total_price: {self.set_total_price()}, "
              f"total_weight: {self.set_total_weight()}")


obj1 = Check()
obj1.set_name("gold")
obj1.set_price(26)
obj1.set_kol(300000)
#
# obj1.set_kol(2)
obj1.get_info()
