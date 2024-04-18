# Задача 1
# file_1 = open('text_1.txt', 'r', encoding='utf-8')
# file_2 = open('text_2.txt', 'r', encoding='utf-8')
#
# list_1 = [i.replace('\n', '') for i in file_1.readlines()]
# list_2 = [i.replace('\n', '') for i in file_2.readlines()]
# for i in range(len(list_1)):
#     if list_1[i] != list_2[i]:
#         print(list_1[i], list_2[i])
# file_1.close()
# file_2.close()


# Задача 2
# file_analysis = open('tex_analysis.txt', 'w', encoding='utf-8')
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as file:
#     number_of_characters = len(file.read().replace(' ', ''))
#     file_analysis.write(f'Количество символов - {number_of_characters} \n')
#
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as file:
#     file_analysis.write(f'Количество строк - {len(file.readlines())}\n')
#
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as file:
#     vowel_letters = 0
#     list_vowel_letters = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
#     for i in file.readlines():
#         for j in i:
#             if j in list_vowel_letters:
#                 vowel_letters += 1
#
#     file_analysis.write(f'Количество гласных букв - {vowel_letters}\n')
#
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as file:
#     consonant_letters = 0
#     list_vowel_letters = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')
#     for i in file.readlines():
#         for j in i:
#             if j not in list_vowel_letters:
#                 consonant_letters += 1
#
#     file_analysis.write(f'Количество согласных букв - {consonant_letters}\n')
#
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as file:
#     quantity_number = 0
#     for i in file.readlines():
#         for j in i:
#             if j in '1234567890':
#                 quantity_number += 1
#
#     file_analysis.write(f'Количество цифр - {quantity_number}')


# Задача 3
# with open('old_file_string.txt', 'r') as file:
#     list_file = file.readlines()
#     with open('new_file_string.txt', 'w') as file_w:
#         for i in range(len(list_file) - 1):
#             file_w.write(list_file[i])


# Задача 4
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as f:
#     long_line = 0
#     for i in f.readlines():
#         if len(i) > long_line:
#             long_line = len(i)
#     print(long_line)


# Задача 5
# input_str = input("Введите слово: ")
# count = 0
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as f:
#     for i in f.readlines():
#         for j in i.split():
#             if input_str == j:
#                 count += 1
# print(f'слово {input_str} встречается {count} раз')


# Задача 6
# with open('tex_for_analysis.txt', 'r', encoding='utf-8') as f:
#     file = f.read()
#     print(file)
#     print('-----------------------------')
#     old_str = input("Введите слово которое хотите заменить: ")
#     new_str = input('Введите новое слово: ')
#     file = file.replace(old_str, new_str)
#
#     with open('tex_for_analysis.txt', 'w', encoding='utf-8') as f:
#         f.write(file)
