#  Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

def Input_number(message):
    number = int(input(message))
    return number

num_S = Input_number('Сумма чисел: ')
num_P = Input_number('Произведение чисел: ')

for x in range(1, 1000):
    y = num_S - x
    if x <= y and x * y == num_P:
        print(f'{num_S}{num_P} -> {x}{y}')
        break
else:
    print('Не угадали, попытайтесь снова!')
    