# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

len_lst = int(input('Задайте длину списка: '))
search_number = int(input('Введите искомое число: '))

lst = [i for i in range(1, len_lst + 1)]
print(lst)

value = 0

for i in range(len(lst)):
    if search_number > lst[i]:
        value = lst[i]

if search_number > lst[-1]:
    print(lst[-1])
else:
    print(value)