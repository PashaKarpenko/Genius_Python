 # У цьому модулі створіть наступні функції:
# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.

def calculate_average(numbers):
    number = 0
    count = 0
    for num in numbers:
        number += num
        count += 1
    return number / count


# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

def find_max(numbers):
    return max(numbers)
