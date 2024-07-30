### Умовні конструкції:
# 1. **Перевірка паролю:**
# Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає
# з ним. Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть
# повідомлення "Неправильний пароль".

password = input("Введіть пароль: ")
if password == "password123":
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")


# 2. **Визначення днів тижня:**
#    Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. Якщо номер
#    дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.

number_of_day = int(input("Введіть номер дня тижня: "))
if 1 <= number_of_day <= 7:
    if number_of_day == 1:
        print("Monday")
    elif number_of_day == 2:
        print("Tuesday")
    elif number_of_day == 3:
        print("Wednesday")
    elif number_of_day == 4:
        print("Thursday")
    elif number_of_day == 5:
        print("Friday")
    elif number_of_day == 6:
        print("Saturday")
    elif number_of_day == 7:
        print("Sunday")
else:
    print("Ви ввели не вірний номер дня тижня.")

# ### Цикли:
#
# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.


number = int(input('Введіть число для генерації таблиці множення: '))
i = 1
while i <= 10:
    result = number * i
    print(result)
    i += 1


# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.

sum_of_numbers = 0
input_string = input('Введіть список чисел через пробіл: ')
number_strings = input_string.split()
list_of_numbers = [int(num) for num in number_strings]
for number in list_of_numbers:
    sum_of_numbers += number
print(sum_of_numbers)


# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.

n = int(input('Введіть число для обчислення факторіала: '))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)


# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.

start = int(input('Введіть початкове число діапазону: '))
end = int(input('Введіть кінцеве число діапазону: '))
prime_numbers = []
for num in range(start, end +1):
    if num > 1:  # Прості числа повинні бути більшими за 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
