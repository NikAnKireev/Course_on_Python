# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

speed = int(input('Введите скорость: '))
distance = int(input('Введите дистанцию: '))

if (distance % speed != 0):
    time = distance//speed+1
else:
    time = distance//speed

print(time)
