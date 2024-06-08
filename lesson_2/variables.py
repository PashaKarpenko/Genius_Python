# 1. Створити змінні таких типів:

# string
string_1 = "Google is an American search engine company, founded in 1998 by Sergey Brin and Larry Page."
string_2 = "Google is an American search engine company,"

# integer
integer_1 = 10
integer_2 = 12

# float
float_1 = 2.0
float_2 = 15.2

# bool
bool_1 = True
bool_2 = False

# list
list_1 = [1, 2, 3, 4]
list_2 = [2, 3, 5, 8]

# dict
dict_1 = {1, True, "string"}
dict_2 = {"string", False, 5, (5, 7, 9)}

# tuple
tuple_1 = (1, 5, 9, 7, 6)
tuple_2 = (2, 3, 4)

# None
some_var = None


# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі

string_integer_comparison = integer_1 <= integer_2 and string_2 in string_1
print(string_integer_comparison)

float_comparison = float_1 <= float_2
print(float_comparison)

bool_comparison = True < False
print(bool_comparison)

list_comparison = list_1 == list_2
print(list_comparison)

print(dict_1 != dict_2 and list_1 in list_2 or tuple_2 == (2, 3, 4))

print(some_var is not None and "Google is an American" in string_2)


# 3. Використати вивчені функції Python:
# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()

num_str = 125
string_from_numb = str(num_str)

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
# усі букви 'y' на '0' та 'i' на '1'.

message = 'Hi, my name is Python!'
message = message.replace('y', 'o').replace("i", '1')

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
# допомогою функції split(),

split_test = 'This is a split test'
split_test = split_test.split()

#а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join

string_join = " ".join(split_test)

#  4. Визначити довжину рядку string_join за допомогою функції len()

print(len(string_join))

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5

list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)

#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])

#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()

print(list_extend.index(6))

#  4. Визначити довжину списку list_append за допомогою функції len()

print(len(list_append))

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where

dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test["where"])

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення

print(dict_test.keys(), dict_test.values())

#  3. За допомогою функції items() вивести на екран пари ключ - значення

print(dict_test.items())
