# Найдите сумму цифр трехзначного числа.

number = int(input('Введите целое трехзначное число:\n'))
sum = 0
if number > 99 and number < 1000:
    while number > 0:
        sum = number % 10 + sum
        number = number // 10
    print(sum)
else:
    print('Вы ввели некорректное число, повторите попытку.')
