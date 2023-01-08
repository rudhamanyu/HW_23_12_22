# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральное число: '))
koef_list = []
my_str = ''
for i in range(k + 1):
    koef_list.append(randint(-100, 100))
    if (koef_list[i] > 0 or koef_list[i] < 0) and k - i > 1:
        my_str += str(koef_list[i]) + f'*x**{k - i} + '
    elif (koef_list[i] > 0 or koef_list[i] < 0) and k - i:
        my_str += str(koef_list[i]) + '*x + '
    elif (koef_list[i] > 0 or koef_list[i] < 0) and not k - i:
        my_str += str(koef_list[i]) + ' = 0'
    elif not koef_list[i] and not k - i:
        my_str += ' = 0'

result = my_str.replace('+  = 0', '= 0').replace('+ -', '- ').replace('1*', '')

print(koef_list)
print(result)

with open('file2.txt', 'w') as data:
    data.writelines(result)
