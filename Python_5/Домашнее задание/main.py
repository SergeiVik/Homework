# name = 'Никита'
# print(name)
# Мы можем получить каждый отдельный элемент строки по индексу
# print(name[3])
# print(name[-2])

# Срезы
# Использование двух чисел позволяет получить подстроку оригинальной строки
# указывая начало и конец.
# Если мы не указываем начало и/или конец, то они "подразумеваются" началом
# и концом строки соответственно
# print(name[3:5])
# print(name[:5])
# print(name[3:])
# print(name[:])
# print(name[-5:])
# print(name[-5:-2])

# У срезов также может быть третий параметр. Если он представлен - это шаг.
# print(name[1::2])
# print(name[5:2:-1])

# Вне зависимости от используемого метода, строка не изменится.
# Мы просто получим копию, которая изменена.
# test = 'hElLo wOrLd!'
# print(test.capitalize())
# print(test.upper())
# print(test.lower())
# print(test.title())
# print(test.swapcase()) все большие маленькие, а маленькие большие
# print(test.find("L")) ищет строку и возвращает его индекс
# print(test.rfind("L")) ищет строку и возвращает его индекс последнего вхождения

# print(test.startswith('hE'))
# print(test.endswith('!'))

# Методы проверки содержимого всей строки целиком
# nums = '123'
# letters = 'abc'
# numlet = '123abc'
# spaces = '   '
# tabs = '\t\t\t'
# ends = '\n\n'


# str.isalpha()
# str.isdigit()
# str.isalnum()
# str.isspace()

# hello = "hello"
# print(hello)
# print(hello.strip()) удаляет пробелы с начала и конца или указанные символы
# print(hello.strip().strip("%"))
# print(hello.strip(" %"))
# print(hello.ljust(20, '.'))
# print(hello.rjust(20, '.'))
# print(hello.center(20, '.'))

# print("Hello World!".replace("World", ''))
# num = 2
# color = "черного"
# print(f'У меня есть {num} собаки')
# print("У меня есть {} собаки {} цвета".format(num, color))

# print('Перенос строки осуществляется с помощью спец. символа \\n')

# import string
#
# print(string.ascii_letters)
# print(string.printable)
# print("✊")

# 1.
# name = input("Введите строку: ")
# print(name[::-1])


# 2.
# text = input("Введите текст: ")
# digits = 0
# letters = 0
# for i in text:
#     if i.isdigit():
#         digits += 1
#     elif i.isalpha():
#         letters += 1
#
# print(f"Всего {digits} чисел и {letters} букв")

# Списки
# nums = list()
# nums = [1, 2, 3, 4, 5, 6, 7]
# print(nums[1])
# Всё, что касается срезов, работает и со списками
# print(nums[2::2])
# print(nums[:])
# print(nums[::-1])
# print(nums[::2])
# print(nums[1::2])
# print(nums[0:1])
# print(nums[6:7])
# print(nums[3:4])
# print(nums[4:])
# print(nums[4:1:-1])
# print(nums[2:5])

# lst = [1, 2, 'hello', 5.6, True, False, [1, 2, 3]]
# print(lst)

# Рекурсия ссылки списка на самого себя
# a = [1, 2, 3]
# a.append(a)
# print(a)

# name = 'Никита'
# print(list(name))

# 3.
# nums = []
# for i in range(5):
#     num = int(input("Введите число для списка: "))
#     nums.append(num)
# x = int(input("Введите число для поиска: "))
# count = 0
# for num in nums:
#     if num == x:
#         count += 1
# print(f'Число {x} встречается {count} раз')

# nums = [1, 2, 3]
# nums2 = [4, 5, 6]
# Методы добавления элементов в список
# list.append(element)
# list.insert(0, element)
# list.extend(list2)
# Методы добавления элементов из списка
# if 3 in nums:
#     nums.remove(3)
# print(list.remove())
# print(list.pop(1))
# del nums[2]

# print(nums)

# 4.
# nums = []
# num = input("Введите число: ")
# while num.lower() != 'стоп':
#     nums.append(int(num))
#     num = input("Введите число: ")
#
# summa = 0
# for num in nums:
#     summa += num
# print("Сумма: ", summa)
# print("Среднее: ", summa/len(nums))
