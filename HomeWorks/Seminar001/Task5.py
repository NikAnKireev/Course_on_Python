# Найдите сумму цифр любого вещественного или целого числа. Можно использовать decimal. Через строку решать нельзя.

number = float(input('Введите вещественое или дробное число:\n'))
sum = 0

while number != int(number):
    number *= 10

while number > 0:
    sum += number % 10
    number //= 10

print(int(sum))