# Задача HARD необязательная
# Имеется список чисел. Создайте список, в который попадают числа,
# описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# Одно число - это не последовательность.

# Пример:

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]

# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]

# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]

from random import randint

number = int(input('Задайте длину списка: '))

lst = [randint(1, 15) for _ in range(number)]

result = set()
result_2 = set()
value_min = value_max = 0
print(lst)

for i in range(0, len(lst)):
    for j in range(1, len(lst)):
        if lst[i] > lst[j] and lst[i] == lst[j]+1:
            value_min = lst[j]
            value_max = lst[i]
            result.add(value_min)
            result.add(value_max)
        elif lst[j] > lst[i] and lst[j] == lst[i]+1:
            value_min = lst[i]
            value_max = lst[j]
            result_2.add(value_min)
            result_2.add(value_max)
if len(list(result)) > len(list(result_2)):
    print(result)
else:
    print(result_2)
