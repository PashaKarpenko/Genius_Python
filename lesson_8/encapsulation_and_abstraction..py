# Завдання 1: Інкапсуляція
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)

class User:

    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    # Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери).

    def get_attr(self):
        return self.__dict__

    def set_attr(self, attr, value):
        self.__dict__[f'_User__{attr}'] = value
        return {attr: self.__dict__[f'_User__{attr}']}

    # Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.


user = User('Pavlo', 'pavlo@mail.com', 'Password12345')
print(user.get_attr())

user.set_attr('name', 'Vadym')
user. set_attr('email', 'vadym@gmail.com')
user .set_attr('password', 'Password_09876')

print(user.get_attr())


# Завдання 2: Абстракція
#
# Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius, pi=3.14):
        self.radius = radius
        self.pi = pi

    def calculate_area(self):
        area = self.pi * self.radius ** 2
        return area


# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle). У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
class Rectangle(Shape):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self):
        area = self.side_a * self.side_b
        return area


class Triangle(Shape):

    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calculate_area(self):
        area = (self.side * self.height) / 2
        return area


# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

circle = Circle(2)
rectangle = Rectangle(3, 10)
triangle = Triangle(5, 4)

print(circle.calculate_area())
print(rectangle.calculate_area())
print(triangle.calculate_area())



# Завдання 3: Користування інкапсуляцією та абстракцією у реальному коді
#
# Розгляньте фрагмент коду з існуючого проекту або бібліотеки та ідентифікуйте в ньому використання інкапсуляції та абстракції. Поясніть, як вони застосовуються і як це допомагає поліпшити читабельність та підтримку коду.