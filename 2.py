# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


with open('file1.txt', 'r') as data:
    my_str1 = data.read()

with open('file2.txt', 'r') as data:
    my_str2 = data.read()


def get_dict(my_str: str):
    new_str1 = my_str.replace('- ', '+-').replace(' ', '').replace('=0', '')
    new_list = new_str1.split('+')
    max_degree = int(new_list[0].split('*')[-1])
    my_dict = {}
    for item in new_list:
        if item.strip('-').isdigit():
            my_dict[0] = int(item)
        elif item.endswith('*x'):
            my_dict[1] = int(item.split('*')[0])
        elif item == 'x':
            my_dict[1] = 1
        elif item == '-x':
            my_dict[1] = -1
        elif item.split('*')[-1].strip('-').isdigit() and item.split('*')[0].strip('-').isdigit():
            my_dict[int(item.split('*')[-1])] = int(item.split('*')[0])
        elif item.split('*')[-1].strip('-').isdigit() and item.startswith('x'):
            my_dict[int(item.split('*')[-1])] = 1
        elif item.split('*')[-1].strip('-').isdigit() and item.startswith('-x'):
            my_dict[int(item.split('*')[-1])] = -1
    return my_dict, max_degree


my_dict1, max_degree1 = get_dict(my_str1)
my_dict2, max_degree2 = get_dict(my_str2)
print(my_dict1)
print(my_dict2)

result = ''
if max_degree1 > max_degree2:
    for i in range(max_degree1 + 1):
        if not i and (my_dict1.get(i, 0) or my_dict2.get(i, 0)):
            result = f'{my_dict1.get(i, 0) + my_dict2.get(i, 0)} = 0'
        elif not i:
            result = f'= 0'
        elif i == 1 and (my_dict1.get(i, 0) or my_dict2.get(i, 0)):
            result = f'{my_dict1.get(i, 0) + my_dict2.get(i, 0)}*x + {result}'
        elif i > 1 and (my_dict1.get(i, 0) or my_dict2.get(i, 0)):
            result = f'{my_dict1.get(i, 0) + my_dict2.get(i, 0)}*x**{i} + {result}'
else:
    for i in range(max_degree2 + 1):
        if not i and (my_dict1.get(i, 0) or my_dict2.get(i, 0)):
            result = f'{my_dict1.get(i, 0) + my_dict2.get(i, 0)} = 0'
        elif not i:
            result = f'= 0'
        elif i == 1 and (my_dict1.get(i, 0) or my_dict2.get(i, 0)):
            result = f'{my_dict1.get(i, 0) + my_dict2.get(i, 0)}*x + {result}'
        elif i > 1 and (my_dict1.get(i, 0) or my_dict2.get(i, 0)):
            result = f'{my_dict1.get(i, 0) + my_dict2.get(i, 0)}*x**{i} + {result}'

result = result.replace('+ = 0', '= 0').replace('1*x', 'x').replace('+ -', '- ')
print(result)

with open('result.txt', 'w') as data:
    data.writelines(result)
