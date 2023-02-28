# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки

# 4 -> 1 2 3 4
# 9

numb = int(input('Введите количество кустов: '))
count = list(map(int, input('Введите количество ягод на кустах: ')))

max_sum = 0

for i in range(numb):
	cur_sum = sum(count[i:i+3])
	if cur_sum > max_sum:
		max_sum = cur_sum
if count[0] + count[-1] + count[-2] > max_sum:
	max_sum = count[0] + count[-1] + count[-2]
if count[0] + count[1] + count[-1] > max_sum:
	max_sum = count[0] + count[1] + count[-1]

print(f'{numb} -> {count}')
print(max_sum)