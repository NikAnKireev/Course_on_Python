# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


# Input: 5

# Output: 120

factorial = int(input('Введите число:\n'))
i = 1
sum = 1

while i <= factorial:
    sum *= i
    i += 1
print(f'Факториал числа {factorial} = {sum}')
