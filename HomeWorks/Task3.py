# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

lucky_ticket = int(input('Проверим счастливый ли у вас билет. Введите номер билета:\n'))
ticket_left = lucky_ticket // 1000
ticket_right = lucky_ticket % 1000
sum_left_ticket = 0
sum_right_ticket = 0

if lucky_ticket < 1000000 and lucky_ticket > 99999:

    while ticket_left > 0:
        sum_left_ticket = ticket_left % 10 + sum_left_ticket
        ticket_left = ticket_left // 10

    while ticket_right > 0:
        sum_right_ticket = ticket_right % 10 + sum_right_ticket
        ticket_right = ticket_right // 10

    if sum_left_ticket == sum_right_ticket:
        print('Поздравляем! Ваш билет счатсливый!')
    else:
        print('Увы, но Ваш билет простой, попробуйте в следующий раз!')
else:
    print('Вы ввели некоректные данные, попробуйте еще раз.')
