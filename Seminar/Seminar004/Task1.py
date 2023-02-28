# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

word = list(map(str, input('Введите элементы множества через пробел: ').split()))
array = set(word)
count = 0

for i in array:
    for j in range(0, len(word)):
        if i == word[j]:
            count += 1
            if count >= 2:
                word[j] = word[j] + '_' + str(count-1)
    count = 0


print(" ".join(word))
