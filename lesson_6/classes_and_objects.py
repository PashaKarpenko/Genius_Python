# **Завдання 1: Створення класу і об'єктів**
# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)

class Animal:

    # Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    # Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.
    def make_sound(self):
        if self.species == 'cat':
            return f'{self.name} say meow'
        if self.species == 'dog':
            return f'{self.name} say gav'
        if self.species == 'bird':
            return f'{self.name} say cvirin`'


# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.


cat = Animal('Murchyuk', 'cat', 5)
dog = Animal('Rex', 'dog', 10)

print(cat.make_sound())
print(dog.make_sound())

# **Завдання 2: Робота з об'єктами**
# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)
#
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self. height = height

    # Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
    def calculate_area(self):
        return self.width * self.height

# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, виведіть площу прямокутників на екран.


object_1 = Rectangle(12, 15)
object_2 = Rectangle(100, 34)

print(object_1.calculate_area())
print(object_2.calculate_area())