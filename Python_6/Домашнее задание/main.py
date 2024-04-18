# name = input("Введите строку: ")
# prepared_name = name.lower().replace(" ", '')
# print(prepared_name)
# if prepared_name == prepared_name[::-1]:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром!")


# a.
# for i in range(9):
#     for j in range(9):
#         if j >= i:
#             print(" *", end='')
#         else:
#             print("  ", end='')
#     print()

# e.
# for i in range(9):
#     for j in range(9):
#         if (i >= j and i + j <= 8) or (j >= i and i + j >= 8):
#             print(" *", end='')
#         else:
#             print("  ", end='')
#     print()

# з.
# for i in range(9):
#     for j in range(9):
#         if j >= i and i + j >= 8:
#             print(" *", end='')
#         else:
#             print("  ", end='')
#     print()

# к.
# for i in range(9):
#     for j in range(9):
#         if i + j >= 8:
#             print(" *", end='')
#         else:
#             print("  ", end='')
#     print()

# Итераторы и Генераторы
# nums = list(range(100))
# print(nums)
# List Comprehension
# nums = [x**2 for x in range(10) if x % 2 == 0]
# print(nums)
# for n in nums:
#     print(n)

# 1. Дано предложение из 5 слов. Необходимо создать список слов
# этого предложения в верхнем регистре, то есть все буквы слов
# должны стать заглавные
# Например: "А роза упала на лапу"
# >> ["А", "РОЗА", "УПАЛА", "НА", "ЛАПУ"]
# Подсказка: для разделения строки на список слов, можно
# использовать str.split()

# string = input()
# upper_words = [word.capitalize() for word in string.split()]
# print(upper_words)

# [print(x**2) for x in range(10)]

# 2. С помощью генератора создайте список из 10 первых
# простых чисел.
# Напоминание: Простые числа - это те, что делятся без остатка
# только на себя и на 1

# Решение через len - длину списка делителей числа
# print([x for x in range(2, 30) if len([i for i in range(2, x//2) if x % i == 0]) == 0])

# Решение через any - проверка, существуют ли хотя бы один целый делитель числа
# print([x for x in range(2, 30) if not any([x % i == 0 for i in range(2, x//2)])])

# nums = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# [[print(x, end=' ') for x in row] for row in nums]
# nums = [[i * 4 + j + 1 for j in range(4)] for i in range(3)]
# for row in nums:
#     print(*row)

# 3.
# nums = [[i * 4 + j + 1 for j in range(4)] for i in range(3)]
# [print(*row, sep='\t') for row in nums]
# print()
# squares = [[i**2 for i in row] for row in nums]
# [print(*row, sep='\t') for row in squares]


# 4.
# nums = [[1 if -1 <= (i - j) <= 1 else 0 for i in range(10)] for j in range(10)]
# for row in nums:
#     print(*row)


# 5.
# for day in range(1, 32):
#     if day % 7 == 0 or day % 7 == 6:
#         continue
#     if day % 7 == 1:
#         print()
#     print(day, end='\t')


# 6.
# import random
# size = int(input("Введите размер матрицы: "))
# matrix = [[random.randint(1, 100) for i in range(size)] for j in range(size)]
# [print(*row, sep='\t') for row in matrix]
#
# minimum = matrix[0][0]
# for i in range(size):
#     for j in range(size):
#         if i == j and minimum > matrix[i][j]:
#             minimum = matrix[i][j]
#
# print("Минимальный элемент:", minimum)

