class Car:

    wheels = 4

    def __init__(self, model, color, owner, year):

        self.model = model
        self.miles = 0
        self.fuel_tank = 0
        self.color = color
        self.owner = owner
        self.year = year

    def get_fuel_tank(self, litr):
        self.fuel_tank += litr
        print(f"Вы залили {litr} литров бензина, итого  {self.fuel_tank} литров у вас в баке")
        return self.fuel_tank

    def drive(self, km):
        litr = km * 0.1
        if self.fuel_tank >= litr:
            print("Мы смело едем")
            self.miles += km
            self.fuel_tank -= litr
        else:
            print("У вас недостаточно бензина")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Поздравляем с новым цветом машины {self.color}")



tesla = Car("Model X", "white", "Nazgul", "2022")
porshe = Car("Cayenne", "red", "Mirlan", "2022")
tesla.get_fuel_tank(40)
tesla.get_fuel_tank(40)
porshe.get_fuel_tank(50)
tesla.drive(400)
porshe.drive(500)
# print(porshe.fuel_tank)
# print(tesla.fuel_tank)

tesla.change_color("black")
tesla.wheels = 6
del tesla.wheels
print(tesla.wheels)
porshe.exous = "noise"

print(tesla.__dict__)
print(porshe.__dict__)

# print(tesla.color)


