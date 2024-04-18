# Задание 1
import random

one_list = [random.randint(1, 50) for i in range(10)]
two_list = [random.randint(1, 50) for i in range(10)]

print(one_list)
print(two_list)

three_list = one_list + two_list
print('Объединенный список', three_list)

list_sort = []
for i in three_list:
    if i in list_sort:
        continue
    else:
        list_sort.append(i)

print('Список без повторений', list_sort)

common_elements = [i for i in one_list if i in two_list]
print('Общие элементы', common_elements)
print('Уникальные элементы', list_sort)
min_max = [min(one_list), max(one_list), min(two_list), max(two_list)]
print('Максимальные и минимальные значения', min_max)
