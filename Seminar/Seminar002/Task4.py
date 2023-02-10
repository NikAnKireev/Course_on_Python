# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

number = int(input('Введите количество арбузов:\n'))
list_watermelon = []


for _ in range(number):
    list_watermelon.append(random.randint(1, 10))
print(list_watermelon)

min_walue = max_walue = 1

for temp in list_watermelon:
    if temp > max_walue:
        max_walue = temp
    temp += 1

    min_walue = max_walue

    for temp in list_watermelon:
        if temp < min_walue:
            min_walue = temp
    temp += 1

print(f'Для себя арбуз - {max_walue}кг\nДля тещи арбуз - {min_walue}кг')
