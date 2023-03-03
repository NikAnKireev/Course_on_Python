# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes

n = int(input("Введите число: "))

def nat_num (n,m):
    if m == 1:
        return True
    elif n%m==0:
        return False
    else:
        return True and nat_num(n,m-1)


print(nat_num(n,n-1))