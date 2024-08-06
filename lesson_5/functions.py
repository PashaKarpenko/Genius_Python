from calculator import subtract, add, multiply, divide

# **Завдання 1: Робота з функціями**
# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень. Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.

number1 = int(input('Введіть перше число: '))
number2 = int(input('Введіть друге число: '))
operation = input('Введіть операцію, яку необхідно здійснити: ')

if operation == '+':
    print(add(number1, number2))

elif operation == '-':
    print(subtract(number1, number2))
elif operation == '*':
    print(multiply(number1, number2))
elif operation == '/':
    print(divide(number1, number2))

