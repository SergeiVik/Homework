# Задание 1
# c = input('Введите строку: ')
# string = ''
# rev_string = ''
# for i in c:
#     if i != ' ':
#         string += i
#
# for i in range(len(string) - 1, -1, -1):
#     rev_string += string[i]
#
# if string.lower() == rev_string.lower():
#     print('Слово является палиндромом.')
# else:
#     print('Слово не является палиндромом.')

# Задание 2
# lst = []
# text = input('Введите текст: ')
# count = int(input('Введите сколько слов хотите поменять: '))
# while len(lst) != count:
#     text_change = input('Введите слова для выделения: ')
#     lst.append(text_change)
#
# text = text.split()
# for i in text:
#     if i in lst:
#         text[text.index(i)] = text[text.index(i)].upper()
# text = ' '.join(text)
# print(text)

# Задание 3
# text = input('Введите текст: ')
# count = 0
# for i in text:
#     if i == '.' or i == '?' or i == '!':
#         count += 1
# print('Предложений в тексте равно:', count)
