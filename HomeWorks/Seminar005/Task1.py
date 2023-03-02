# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def Pow_Number(arg1, arg2):
    if arg2 == 0:
        return 1
    return arg1*Pow_Number(arg1, arg2-1)

A = int(input("Введите число А: "))
B = int(input("Введите число В: "))

print(f'A = {A}; B = {B} -> {Pow_Number(A, B)}')
