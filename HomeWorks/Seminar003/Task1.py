# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

len_lst = int(input('Задайте длину списка: '))
search_number = int(input('Введите искомое число: '))

lst = [i for i in range(1, len_lst + 1)]
print(lst)

count = 0

for i in range(len(lst)):
    if search_number == lst[i]:
        count += 1

if count == 0:
    print("Такого числа нет.")
else:
    print(count)