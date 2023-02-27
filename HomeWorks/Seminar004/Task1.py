# : Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

n = int(input('Введите количество элементов первого множества: '))
lst_n = [randint(1, 100) for _ in range(n)]

m = int(input('Введите количество элементов второго множества: '))
lst_m = [randint(1, 100) for _ in range(m)]

user = list(map(int, input('Введите элементы множества через пробел: ').split()))

print(lst_n)
print(lst_m)
print(user)
print()

n = set(lst_n)
m = set(lst_m)
user = set(user)

first_merg = n.intersection(m)
second_merg = n.union(m).intersection(user)
third_merg = first_merg.union(second_merg)

print(sorted(third_merg))