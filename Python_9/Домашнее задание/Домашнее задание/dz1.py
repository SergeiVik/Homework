# Задание 1
tup1 = (1, 2, 5, 6, 7)
tup2 = (3, 2, 5, 1, 4)
tup3 = (4, 2, 5, 3, 10)

general_element = [i for i in tup1 if i in tup2 and i in tup3]
unique_element = []
# Задание 3
general_element_and_position = [i for i in tup1 if
                                i in tup2 and i in tup3 and tup1.index(i) == tup2.index(i) and tup1.index(
                                    i) == tup3.index(i)]
# Задание 2
for i in tup1:
    if i not in tup2 and i not in tup3:
        unique_element.append(i)

for i in tup2:
    if i not in tup1 and i not in tup3:
        unique_element.append(i)

for i in tup3:
    if i not in tup1 and i not in tup2:
        unique_element.append(i)

print('Общие элементы -', *general_element)
print('Уникальные элементы -', *unique_element)
print('Уникальные элементы и находятся на одной позиции -', *general_element_and_position)
