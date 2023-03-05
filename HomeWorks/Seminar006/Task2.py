# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

from random import randint

number = int(input('Задайте длину массива: '))
my_array = [randint(-5, 20) for i in range(number)]
print(my_array)

minimum = int(input('Задайте минимальный диапазон: '))
maximum = int(input('Задайте максимальный диапазон: '))

def search_span(arr, mini, maxi):
    array = []
    for i in range(len(arr)):
        if arr[i] >= mini and arr[i] <= maxi:
            array.append(i)
    if len(array) == 0:
        return 'Индексов из заданного диапазона не найдено'
    else:
        return array

print(search_span(my_array, minimum, maximum))

