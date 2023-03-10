# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения
# списка или список задан изначально

from random import randint

number = int(input('Задайте длину списка: '))
k = int(input('На сколько будем сдвигать последовательность: '))

lst = [randint(-10, 10) for _ in range(number)]
print(f"{lst} - было")

for i in range(k):
    lst.insert(0, lst.pop())
print(f"{lst} - стало")

result = [i for i in lst if i > 0]
print(result)