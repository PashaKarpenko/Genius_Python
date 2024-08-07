# **Завдання 1: Наслідування**
# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо. Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту. Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.

    def display_info(self):
        return f'{self.make} {self.model} {self.year} року виробництва'

class Car(Vehicle):
    def __init__(self, make, model, year, count_of_doors) -> None:
        super().__init__(make, model, year)
        self.count_of_doors = count_of_doors

    def open_door(self):
        return 'Your door is open'

    # **Завдання 2: Поліморфізм**
    # Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
    def display_info(self):
        return f'{self.make} {self.model} {self.year} року виробництва, в неї {self.count_of_doors} дверей'


class Bicycle(Vehicle):
    def __init__(self, make, model, year, pedals) -> None:
        super().__init__(make, model, year)
        self.pedals = pedals

    def spin_pedals(self):
        return 'Your bicycle is moving'

    def display_info(self):
        return f'{self.make} {self.model} {self.year} року виробництва, в нього {self.pedals} педалі'

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, count_of_weels) -> None:
        super().__init__(make, model, year)
        self.count_of_weels = count_of_weels

    def move(self):
        return 'Your motorcycle is moving'

    def display_info(self):
        return f'{self.make} {self.model} {self.year} року виробництва, в нього {self.count_of_weels} колеса'

# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.


car = Car('Audi', 'A4', 2015, 5)
bicycle = Bicycle('ХВЗ', 'Україна', 2001, 2)
motorcykle = Motorcycle('BMW', 'V2.0', 2010, 2)

print(car.open_door())
print(motorcykle.move())
print(bicycle.spin_pedals())


# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.
# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта, і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.

print(car.display_info())
print(motorcykle.display_info())
print(bicycle.display_info())
