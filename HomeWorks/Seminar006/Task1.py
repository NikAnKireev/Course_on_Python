# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

number = int(input('Введите первый член арфиметической прогрессии: '))
diff = int(input('Введите разность: '))
lenght = int(input('Введите количество элементов массива: '))


def arith_pro(numb, order, size):
    arr = []
    for i in range(size+1):
        if i != 0:
            arr.append(numb + (i-1)*order)
        else:
            i += 1
    print(arr)

arith_pro(number, diff, lenght)