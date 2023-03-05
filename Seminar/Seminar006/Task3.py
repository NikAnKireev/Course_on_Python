# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:         Вывод:
# 1 2 3 2 3     2

from random import randint

def pair(lst):
    count = 0
    myset = set(lst)
    for i in myset:
        x = lst.count(i)
        count += x // 2
    return count


n = int(input('Введите количество элементов списка: '))
lst1 = [randint(1, 9) for _ in range(n)]
print(lst1)
print(pair(lst1))