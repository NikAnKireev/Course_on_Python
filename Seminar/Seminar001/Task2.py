# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

math_class = int(input('Сколько математических классов вам нужно?\n'))
count = 0
desks = 0

while (count < math_class):
    study = int(input(f'Сколько учеников в классе {count+1}?\n'))
    count = count + 1
    desks = desks + study
print()
print(f'Минимальное количество парт для учеников - {round(desks/2)}')
