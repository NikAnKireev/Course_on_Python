# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

def Input_number(message):
    number = int(input(message))
    return number


number = Input_number('Задайте число: ')
count = 1

while count <= number:
    print(f'{count}', end=' ')
    count *= 2