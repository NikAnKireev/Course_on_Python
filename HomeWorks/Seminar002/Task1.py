# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

import random

def Input_List(mesage):
    number = int(input(mesage))
    list_coins = []
    for _ in range(number):
        list_coins.append(random.randint(0, 1))
    return list_coins

coins_list = Input_List('Введите количество монет:\n')
print(coins_list)

def Serch_Value(list, arg):
    count = 0
    for temp in list:
        if arg == temp:
            count +=1
    temp = +1
    return count
    
coins_tails = 0
coins_eagle = 1

value_first = Serch_Value(coins_list, coins_tails)
value_second = Serch_Value(coins_list, coins_eagle)

if value_first < value_second:
    print(value_first)
else:
    print(value_second)